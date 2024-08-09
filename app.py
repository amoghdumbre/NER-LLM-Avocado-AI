import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mistralai import Mistral

# Load your API key from environment variables
api_key = os.environ["MISTRAL_API_KEY"]  # Replace with your actual Mistral API key

# Initialize the Mistral client
client = Mistral(api_key=api_key)

# Initialize FastAPI
app = FastAPI()

# Define the Pydantic model for the input data
class ArticleInput(BaseModel):
    title: str
    content: str

# Your agent ID
agent_id = "ag:3c2c02ed:20240809:untitled-agent:6b1d8fa7"

# Function to clean up the processed_output
def clean_json_output(output):
    # Remove triple backticks and unwanted newlines
    output = output.replace('```json', '').replace('```', '').strip()
    # Correct indentation and format
    return json.loads(output)

# Endpoint to process article text
@app.post("/process_article/")
async def process_article(article: ArticleInput):
    # Construct the prompt
    prompt = f"""
    Process the following text and output only the following:

    1. Named Entity Recognition (NER) results: List the identified medical terms, conditions, and treatments.

    2. Key Phrase Extraction: List the main topics and significant claims.

    Output the results in JSON format with no additional commentary.

    Text:
    \"\"\"
    {article.content}
    \"\"\"
    """

    try:
        # Send the request to the Mistral API using your agent
        chat_response = client.agents.complete(
            agent_id=agent_id,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        # Extract the processed output as text and strip leading/trailing whitespace
        processed_output = chat_response.choices[0].message.content.strip()

        # Clean and parse the JSON output
        cleaned_output = clean_json_output(processed_output)

        # Return the structured response
        return {
            "title": article.title,
            "processed_output": cleaned_output
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
