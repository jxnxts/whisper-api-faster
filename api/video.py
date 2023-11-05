from moviepy.editor import VideoFileClip
import os

def extract_audio_from_video(file_path):
    # Create a VideoFileClip object
    clip = VideoFileClip(file_path)

    # Extract the filename (without directories) from file_path
    file_name = os.path.basename(file_path)

    # Create the audio_path using the extracted file_name
    audio_path = "uploads/" + file_name + ".mp3"

    # Write the audio file
    clip.audio.write_audiofile(audio_path)
    
    return audio_path

