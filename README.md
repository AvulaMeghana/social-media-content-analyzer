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
