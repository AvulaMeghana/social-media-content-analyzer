from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel

from backend.services.pdf_extractor import extract_text_from_pdf
from backend.services.ocr import extract_text_from_image
from backend.services.nlp_analyzer import analyze_content

app = FastAPI(
    title="Social Media Content Analyzer",
    description="API for extracting and analyzing social media content",
    version="1.0.0"
)
app.mount(
    "/app",
    StaticFiles(directory="frontend", html=True),
    name="frontend"
)

# Folder where uploaded files will temporarily be stored
UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Social Media Content Analyzer API is running"
    }


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    # Check file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    try:
        # Save uploaded PDF
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Extract text
        extracted_text = extract_text_from_pdf(str(file_path))

        # Check whether text was extracted
        if not extracted_text:
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the PDF."
            )

        return {
            "filename": file.filename,
            "text": extracted_text
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing PDF: {str(e)}"
        )

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG, PNG, and WEBP images are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    try:
        # Save uploaded image
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Extract text using OCR
        extracted_text = extract_text_from_image(str(file_path))

        if not extracted_text:
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the image."
            )

        return {
            "filename": file.filename,
            "text": extracted_text
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )

class TextInput(BaseModel):
    text: str


@app.post("/analyze")
async def analyze_text(data: TextInput):

    if not data.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )

    try:
        analysis = analyze_content(data.text)

        return {
            "text": data.text,
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing content: {str(e)}"
        )

@app.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):

    allowed_extensions = {
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    }

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, JPG, JPEG, PNG, and WEBP files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    try:
        # Save uploaded file
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # -------------------------
        # Extract text
        # -------------------------

        if file_extension == ".pdf":
            extracted_text = extract_text_from_pdf(str(file_path))
            source_type = "PDF"

        else:
            extracted_text = extract_text_from_image(str(file_path))
            source_type = "Image"

        # -------------------------
        # Check extracted text
        # -------------------------

        if not extracted_text:
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the file."
            )

        # -------------------------
        # NLP analysis
        # -------------------------

        analysis = analyze_content(extracted_text)

        # -------------------------
        # Return complete result
        # -------------------------

        return {
            "filename": file.filename,
            "source_type": source_type,
            "extracted_text": extracted_text,
            "analysis": analysis
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing file: {str(e)}"
        )