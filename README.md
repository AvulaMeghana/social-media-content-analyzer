Social Media Content Analyzer

A web-based application that extracts and analyzes text from social media content uploaded as PDF documents or images.

The application combines PDF text extraction, Optical Character Recognition (OCR), and Natural Language Processing (NLP) to provide useful insights from uploaded content.

Features
Upload PDF files
Upload JPG, JPEG, PNG, and WEBP images
Extract text from PDF documents
Extract text from images using OCR
Analyze extracted content using NLP
Sentiment analysis
Word count
Sentence count
Hashtag detection
Keyword extraction
Call-to-action detection
Readability analysis
Engagement score
Content improvement suggestions
Technology Stack
Backend
Python
FastAPI
PyMuPDF
Tesseract OCR
TextBlob
textstat
Frontend
HTML
CSS
JavaScript
Tools
Git
GitHub
Uvicorn
Architecture

The application follows this processing flow:

User Upload
     ↓
File Type Detection
     ↓
Text Extraction
     ↓
NLP Analysis
     ↓
Content Insights
     ↓
Results Dashboard
PDF Processing

PDF files are processed using PyMuPDF to extract text from the document.

Image Processing

Image files are processed using Tesseract OCR to recognize and extract text from images.

NLP Processing

The extracted text is analyzed using NLP techniques to generate:

Sentiment
Keywords
Hashtags
Word count
Sentence count
Readability score
Engagement score
Call-to-action detection
Content improvement suggestions
Project Structure
social-media-content-analyzer/
│
├── backend/
│   ├── main.py
│   └── services/
│       ├── nlp_analyzer.py
│       ├── ocr.py
│       └── pdf_extractor.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── requirements.txt
└── README.md
How to Run the Project

Follow these steps to run the project after downloading it from GitHub.

Prerequisites

Make sure the following are installed on your computer:

Python 3.13 or later
Tesseract OCR
Step 1: Download the Project

Open the GitHub repository and download the project as a ZIP file.

Extract the ZIP file and open the extracted project folder.

The project folder should contain:

backend/
frontend/
.gitignore
README.md
requirements.txt
Step 2: Open Command Prompt

Open Command Prompt inside the extracted project folder.

If Command Prompt is opened in another location, navigate to the project folder using:

cd path\to\social-media-content-analyzer-main
Step 3: Check Python Installation

Check whether Python is installed:

python --version

Python 3.13 or later is recommended.

Step 4: Create a Virtual Environment

Create a virtual environment for the project:

python -m venv venv

This creates a venv folder inside the project directory.

Step 5: Activate the Virtual Environment

For Windows, run:

venv\Scripts\activate

After successful activation, (venv) should appear at the beginning of the command prompt.

Example:

(venv) C:\Users\YourName\Downloads\social-media-content-analyzer-main>
Step 6: Install Dependencies

Install all required Python packages using the provided requirements.txt file:

pip install -r requirements.txt

This installs the dependencies required by the backend application.

Step 7: Verify Tesseract OCR

Tesseract OCR is required for extracting text from images.

Check whether Tesseract is installed and available in the system PATH:

tesseract --version

If the Tesseract version is displayed, OCR is ready to use.

If tesseract is not recognized, install Tesseract OCR and add its installation directory to the system PATH.

After changing the PATH, restart Command Prompt and run:

tesseract --version

again.

Step 8: Start the Application

Make sure the virtual environment is active.

Start the FastAPI server using:

uvicorn backend.main:app --reload

The terminal should display a message similar to:

Uvicorn running on http://127.0.0.1:8000
Application startup complete.

Keep this terminal window running while using the application.

Step 9: Open the Application

Open a web browser and visit:

http://127.0.0.1:8000/app/

The Social Media Content Analyzer interface will open.

API Documentation

The application is built using FastAPI and provides interactive API documentation.

Open:

http://127.0.0.1:8000/docs

The FastAPI documentation allows you to view and test the available API endpoints.

API Endpoints
Home
GET /

Checks whether the API is running.

Upload PDF
POST /upload-pdf

Uploads a PDF file and extracts its text.

Upload Image
POST /upload-image

Uploads an image and extracts text using Tesseract OCR.

Supported image formats:

JPG
JPEG
PNG
WEBP
Analyze Text
POST /analyze

Analyzes the provided text using NLP.

Analysis Features

After text is extracted, the application provides the following analysis:

Sentiment Analysis

Analyzes the overall sentiment of the content.

Word Count

Calculates the number of words in the extracted content.

Sentence Count

Calculates the number of sentences in the content.

Hashtag Detection

Detects hashtags present in the content.

Keyword Extraction

Identifies important keywords from the content.

Call-to-Action Detection

Detects call-to-action content in the text.

Readability Analysis

Provides a readability measurement for the extracted content.

Engagement Score

Generates an engagement score based on the analyzed content.

Content Improvement Suggestions

Provides suggestions to improve the quality and effectiveness of the social media content.

Application Workflow
PDF / Image
     ↓
File Upload
     ↓
File Type Detection
     ↓
Text Extraction
     ↓
PDF → PyMuPDF
Image → Tesseract OCR
     ↓
Extracted Text
     ↓
NLP Analysis
     ↓
Sentiment / Keywords / Hashtags / Readability
     ↓
Engagement Score
     ↓
Improvement Suggestions
     ↓
Results Dashboard
File Handling

Uploaded files are temporarily stored for processing.

The following files and folders are excluded from Git using .gitignore:

venv/
__pycache__/
*.pyc
.env
backend/uploads/

The virtual environment is intentionally not included in the GitHub repository because it can be recreated using:

python -m venv venv
Troubleshooting
Python is not recognized

Run:

python --version

If Python is not recognized, install Python and make sure Python is added to the system PATH.

Restart Command Prompt after installation.

Tesseract is not recognized

Run:

tesseract --version

If Tesseract is not recognized, install Tesseract OCR and add its installation directory to the system PATH.

Restart Command Prompt after modifying the PATH.

Dependencies are not installed

Make sure the virtual environment is activated.

You should see (venv) at the beginning of the command prompt.

Then run:

pip install -r requirements.txt
Application does not start

Make sure:

You are inside the project folder.
The virtual environment is activated.
Dependencies are installed.
Tesseract OCR is installed.

Then run:

uvicorn backend.main:app --reload
Application page does not open

Make sure the FastAPI server is still running in the terminal.

Then open:

http://127.0.0.1:8000/app/
API documentation does not open

Make sure the server is running.

Then open:

http://127.0.0.1:8000/docs
Future Enhancements

Possible future improvements include:

Support for additional social media platforms
Advanced content analytics
Data visualization dashboards
Analysis history
User authentication
Improved keyword extraction
Advanced sentiment analysis
Content performance prediction
Database integration
Cloud deployment
Author

Developed as a technical assignment for Unthinkable.
