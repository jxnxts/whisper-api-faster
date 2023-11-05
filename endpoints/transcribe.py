
from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi.security import HTTPBearer, SecurityScopes
from fastapi import Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from models.contrato import Contrato
from auth.token import authenticate_token
import base64
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from faster_whisper import WhisperModel, decode_audio
from moviepy.editor import VideoFileClip
from urllib.parse import urlparse
from tempfile import NamedTemporaryFile
import requests
import os
from api.video import extract_audio_from_video


router = APIRouter(tags=['transcribe'], responses={
                   404: {"description": "Not found"}})


@app.post("/transcribe")
async def transcribe_audio(file_url: str):
    # Parse the URL to get the filename and extension
    parsed_url = urlparse(file_url)
    file_name = os.path.basename(parsed_url.path)

    # Check if the file extension is supported
    allowed_extensions = [".mp4", ".mp3", ".ogg", ".wav", ".mov"]
    if not any(file_name.endswith(ext) for ext in allowed_extensions):
        return {"error": "Unsupported file format"}

    # Download the file from the URL
    r = requests.get(file_url)
    if r.status_code != 200:
        return {"error": "Error downloading file"}

    # Save the downloaded file to disk
    with NamedTemporaryFile(delete=False, suffix=file_name) as f:
        f.write(r.content)
    file_path = f.name

    # Extract audio from video if applicable
    if file_name.endswith(".mp4") or file_name.endswith(".mov"):
        audio_path = extract_audio_from_video(file_path)
    else:
        audio_path = file_path

    # Transcribe the audio using faster-whisper
    model = WhisperModel("large-v2")  # Choose the desired model
    segments, _ = model.transcribe(audio_path)

    # Get the transcriptions
    transcriptions = [segment.text for segment in segments]

    return {"transcriptions": transcriptions}
