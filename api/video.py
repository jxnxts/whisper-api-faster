from fastapi import FastAPI
from faster_whisper import WhisperModel, decode_audio
from moviepy.editor import VideoFileClip
from urllib.parse import urlparse
from tempfile import NamedTemporaryFile
import requests
import os


def extract_audio_from_video(video_path):
    clip = VideoFileClip(video_path)
    audio_path = f"uploads/{clip.filename}.mp3"
    clip.audio.write_audiofile(audio_path)
    return audio_path