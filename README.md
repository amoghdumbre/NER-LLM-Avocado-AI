# NER-LLM-Avocado-AI
This repository contains a Python-based solution for extracting articles on menstrual health from Flo's blog, analyzing them using an LLM for NER and key phrase extraction, and providing the analysis via a FastAPI endpoint. The project is a scalable prototype for medical text processing.
# NER-LLM-Avocado-AI

## Overview
This repository contains a Python-based solution for extracting articles on menstrual health and contraception from the Flo app's blog, analyzing the content using a Large Language Model (LLM) for Named Entity Recognition (NER) and key phrase extraction, and providing the results via a FastAPI endpoint. The project is a functional prototype designed for processing and analyzing medical texts.

## Approach

### 1. Environment Setup
- **Objective:** Set up the environment required for web scraping and NLP analysis.
- **Implementation:** The notebook installs necessary packages, including Google Chrome for Selenium-based web scraping. ChromeDriver is installed and configured to work in a headless mode for efficiency.

### 2. Content Extraction
- **Objective:** Extract articles related to menstrual health or contraception from the Flo app's blog.
- **Implementation:**
  - Selenium is used to navigate the Flo blog and scrape article links, titles, publication dates, and content.
  - The script extracts the first five articles meeting the criteria, stores the metadata and content in both JSON and CSV formats.

### 3. LLM-Powered Content Analysis
- **Objective:** Perform NLP tasks such as Named Entity Recognition (NER) and key phrase extraction on the extracted content.
- **Implementation:**
  - The Mistral AI model is utilized for processing the extracted articles.
  - Prompts are crafted to instruct the LLM to identify medical terms, conditions, treatments, and extract key phrases relevant to the article content.
  - The processed results are stored in a structured JSON format.

### 4. API Development
- **Objective:** Develop a FastAPI endpoint that accepts article text as input and returns the results of the NLP tasks.
- **Implementation:**
  - FastAPI is used to create an API that processes input text and returns structured JSON output with NER and key phrase extraction results.
  - The API is designed to be easily extendable for further enhancements.

## Challenges Faced
- **Web Scraping:** Handling dynamic content and inconsistent class naming on the Flo blog required careful handling within Selenium to ensure accurate extraction.
- **LLM Integration:** Tuning the LLM for precise identification of medical entities and key phrases required iterative adjustments to the prompt structure.
- **Environment Configuration:** Ensuring that all dependencies, particularly for web scraping, were correctly configured in the Colab environment.

## Ideas for Scaling the System
- **Enhanced Scraping:** Expand the scraping capability to cover more sources and handle a wider variety of content structures.
- **Custom LLM Fine-Tuning:** Train a custom LLM model specifically on medical literature to improve the accuracy and relevance of entity recognition and key phrase extraction.
- **API Extension:** Deploy the API to a cloud platform with autoscaling, and add batch processing capabilities to handle larger volumes of data and requests.

## Setup Instructions
1. **Clone the repository:**
    ```bash
    git clone https://github.com/YourGitHubUsername/NER-LLM-Avocado-AI.git
    cd NER-LLM-Avocado-AI
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the scraper:**
    ```bash
    python floscraper.py
    ```
4. **Start the FastAPI server:**
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    ```
5. **Access the API documentation:**
   Visit `http://localhost:8000/docs` to interact with the API.

## Deliverables
- **Codebase:** Python scripts for content extraction (`floscraper.py`), LLM analysis, and API development.
- **Data Files:** Extracted articles in JSON/CSV format and processed analysis results.
- **Video Demonstration:** A 5-minute video showcasing the functionality of the system.



