# Social Media Content Analyzer

A web-based application that extracts and analyzes text from social media content uploaded as PDF documents or images.

The application combines PDF text extraction, Optical Character Recognition (OCR), and Natural Language Processing (NLP) to provide useful insights from uploaded content.

---

## Features

- Upload PDF files
- Upload JPG, JPEG, PNG, and WEBP images
- Extract text from PDF documents
- Extract text from images using OCR
- Analyze extracted content using NLP
- Sentiment analysis
- Word count
- Sentence count
- Hashtag detection
- Keyword extraction
- Call-to-action detection
- Readability analysis
- Engagement score
- Content improvement suggestions

---

## Technology Stack

### Backend

- Python
- FastAPI
- PyMuPDF
- Tesseract OCR
- TextBlob
- textstat

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Git
- GitHub
- Uvicorn

---

## Architecture

The application follows this processing flow:

```text
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
```

---

## Project Structure

```text
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
```

---

# How to Run the Project

Follow these steps to run the project after downloading it from GitHub as a ZIP file.

## Prerequisites

Make sure the following are installed on your computer:

- Python 3.13 or later
- Tesseract OCR

---

## Step 1: Download the Project

1. Download the project from GitHub as a ZIP file.
2. Extract the ZIP file.
3. Open the extracted project folder.
4. Make sure the folder contains:

```text
backend/
frontend/
README.md
requirements.txt
.gitignore
```

---

## Step 2: Open Command Prompt

Open Command Prompt inside the project folder.

The Command Prompt should be opened in the folder containing `requirements.txt`.

You can check the folder using:

```cmd
dir
```

You should see:

```text
backend
frontend
README.md
requirements.txt
.gitignore
```

---

## Step 3: Create a Virtual Environment

Run:

```cmd
python -m venv venv
```

---

## Step 4: Activate the Virtual Environment

For Windows, run:

```cmd
venv\Scripts\activate
```

After successful activation, `(venv)` should appear at the beginning of the command prompt.

Example:

```text
(venv) C:\Users\YourName\Downloads\social-media-content-analyzer-main>
```

---

## Step 5: Install Dependencies

Run:

```cmd
pip install -r requirements.txt
```

This installs all the Python packages required by the project.

---

## Step 6: Verify Tesseract OCR

Tesseract OCR is required for extracting text from images.

Run:

```cmd
tesseract --version
```

If the Tesseract version is displayed, OCR is ready to use.

If Tesseract is not recognized, install Tesseract OCR and add its installation directory to the system PATH.

---

## Step 7: Start the Application

Run:

```cmd
uvicorn backend.main:app --reload
```

The terminal should display something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

Keep the Command Prompt window running while using the application.

---

## Step 8: Open the Application

Open a web browser and visit:

```text
http://127.0.0.1:8000/app/
```

The Social Media Content Analyzer application will open.

---

# API Documentation

The application uses FastAPI and provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The documentation allows users to view and test the available API endpoints.

---

# API Endpoints

## Home

```text
GET /
```

Checks whether the API is running.

## Upload PDF

```text
POST /upload-pdf
```

Uploads a PDF file and extracts its text.

## Upload Image

```text
POST /upload-image
```

Uploads an image and extracts text using Tesseract OCR.

Supported image formats:

- JPG
- JPEG
- PNG
- WEBP

## Analyze Text

```text
POST /analyze
```

Analyzes the provided text using NLP.

---

# Analysis Features

### Sentiment Analysis

Analyzes the overall sentiment of the content.

### Word Count

Calculates the number of words in the content.

### Sentence Count

Calculates the number of sentences in the content.

### Hashtag Detection

Detects hashtags present in the content.

### Keyword Extraction

Identifies important keywords from the content.

### Call-to-Action Detection

Detects call-to-action content in the text.

### Readability Analysis

Provides a readability measurement for the content.

### Engagement Score

Generates an engagement score based on the analyzed content.

### Content Improvement Suggestions

Provides suggestions to improve the quality and effectiveness of the social media content.

---

# Application Workflow

```text
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
```

---

# File Handling

Uploaded files are temporarily stored for processing.

The following files and folders are excluded from Git using `.gitignore`:

```text
venv/
__pycache__/
*.pyc
.env
backend/uploads/
```

The virtual environment is not included in the GitHub repository because it can be recreated using:

```cmd
python -m venv venv
```

---

# Troubleshooting

## Python is not recognized

Run:

```cmd
python --version
```

If Python is not recognized, install Python and make sure Python is added to the system PATH.

---

## Tesseract is not recognized

Run:

```cmd
tesseract --version
```

If Tesseract is not recognized, install Tesseract OCR and add its installation directory to the system PATH.

Restart Command Prompt after modifying the PATH.

---

## Requirements file is not found

Make sure Command Prompt is opened inside the project folder containing `requirements.txt`.

Run:

```cmd
dir
```

You should see:

```text
backend
frontend
README.md
requirements.txt
```

Then run:

```cmd
pip install -r requirements.txt
```

---

## Application does not start

Make sure the virtual environment is activated and run:

```cmd
uvicorn backend.main:app --reload
```

---

## Application page does not open

Make sure the FastAPI server is still running in the terminal.

Then open:

```text
http://127.0.0.1:8000/app/
```

---

## API documentation does not open

Make sure the server is running.

Then open:

```text
http://127.0.0.1:8000/docs
```

---

# Future Enhancements

- Support for additional social media platforms
- Advanced content analytics
- Data visualization dashboards
- Analysis history
- User authentication
- Improved keyword extraction
- Advanced sentiment analysis
- Database integration
- Cloud deployment

---

# Author

Developed as a technical assignment for Unthinkable.
