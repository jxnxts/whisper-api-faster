
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
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
load_dotenv()  # take environment variables from .env.


router = APIRouter(tags=['transcribe'], responses={
                   404: {"description": "Not found"}})

@router.post("/transcribe")
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
    if file_name.endswith(".mp4") or file_name.endswith(".mov"):
        # check if the uploads directory exist if not create one
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        
        audio_path = extract_audio_from_video(file_path)
    else:
        audio_path = file_path

    # Transcribe the audio using faster-whisper
    model = WhisperModel(os.getenv("MODEL"), device=os.getenv("DEVICE"), compute_type=os.getenv("COMPUTETYPE"))  # Choose the desired model    # model = WhisperModel("large-v2", device="cpu", compute_type="int8")  # Choose the desired model
    vad_filter = os.getenv("VADFILTER")
    vad_filter = vad_filter.lower() in ['true', '1', 't', 'y', 'yes']  # This converts the string to a boo
    segments, _ = model.transcribe(audio_path, beam_size=5, vad_filter=vad_filter, vad_parameters=dict(min_silence_duration_ms=500))

    # Get the transcriptions
    transcriptions = [segment.text for segment in segments]

    return {"transcriptions": transcriptions}
