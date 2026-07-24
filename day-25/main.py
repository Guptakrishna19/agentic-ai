import os

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from rag import index_document, ask_rag


load_dotenv()

app = FastAPI(
    title="RAG Document Q&A API"
)


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Create uploads folder
UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


class QuestionRequest(BaseModel):

    question: str


@app.get("/")
def home():

    return FileResponse(
        "index.html"
    )


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    # Only allow TXT files
    if not file.filename.endswith(".txt"):

        return {
            "error": "Only .txt files are supported."
        }

    # Read uploaded file
    content = await file.read()

    text = content.decode(
        "utf-8"
    )

    # Save file
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)

    # Add document to RAG
    chunk_count = index_document(
        text,
        file.filename
    )

    return {
        "message": "Document uploaded and indexed successfully.",
        "filename": file.filename,
        "chunks": chunk_count
    }


@app.post("/ask")
def ask_question(
    request: QuestionRequest
):

    result = ask_rag(
        request.question
    )

    return result