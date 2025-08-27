from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from models import Document
from database import get_db
from utils import extract_pdf_text, get_ai_insight, fallback_insight
from database import SessionLocal, engine, Base

import shutil, os

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_pdf_text(file_path)
    insight = get_ai_insight(text) or fallback_insight(text)
    
    db = SessionLocal()
    doc = Document(filename=file.filename, insight=insight)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    db.close()
    return {"doc_id": doc.id, "insight": insight, "filename": file.filename}

@app.get("/insights")
def get_insights(doc_id: int = Query(...)):
    db = SessionLocal()
    doc = db.query(Document).filter_by(id=doc_id).first()
    db.close()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found.")
    return {"doc_id": doc.id, "insight": doc.insight, "filename": doc.filename}

@app.get("/history")
def get_history():
    db = SessionLocal()
    docs = db.query(Document).order_by(Document.id.desc()).all()
    result = [{"id": d.id, "filename": d.filename, "insight": d.insight} for d in docs]
    db.close()
    return result
