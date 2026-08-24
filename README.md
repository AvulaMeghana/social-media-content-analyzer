# Social Media Content Analyzer

A web-based application that extracts and analyzes text from social media content uploaded as PDF documents or images.

## Features

- Upload PDF files
- Upload JPG, JPEG, PNG, and WEBP images
- Extract text from PDF documents
- Extract text from images using OCR
- Analyze extracted content using NLP
- Sentiment analysis
- Word and sentence count
- Hashtag detection
- Keyword extraction
- Call-to-action detection
- Readability analysis
- Engagement score
- Content improvement suggestions

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

## Architecture

The application follows this flow:

Upload File → Text Extraction → NLP Analysis → Results Dashboard

PDF files are processed using PyMuPDF, while image files are processed using Tesseract OCR. The extracted text is then analyzed using NLP techniques.

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
