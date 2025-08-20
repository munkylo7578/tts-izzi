from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from openai import OpenAI

app = FastAPI()

# Allow frontend requests (CORS fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/tts")
def tts(text: str = "This is OpenAI TTS served as a blob."):
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )
    audio_bytes = response.read()
    return Response(content=audio_bytes, media_type="audio/mpeg")
