# Step 1: Setup audio recorder (ffmpeg & portaudio)
#dependencies- ffmpeg,portaudio,pyaudio
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 2: Record and save audio
def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Record audio from microphone and save as MP3 file.

    Args:
        file_path (str): Path to save recorded audio.
        timeout (int): Max time for phrase to start (in seconds).
        phrase_time_limit (int): Max time for phrase recording (in seconds).
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            # Record audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Convert recorded audio to MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_filepath="patient_voice_test.mp3"
#record_audio(file_path=audio_filepath)

# Run recording function
#record_audio(file_path="patient_voice_test.mp3")

#step 3:Setup speech to text-STT-model for transcription
import os
from groq import Groq


#Setup speech to te
GROQ_API_KEY= os.environ.get("GROQ_API_KEY")
stt_model ="distil-whisper-large-v3-en"

def transcribe_with_groq(stt_model,audio_filepath,GROQ_API_KEY):
    client = Groq(api_key = GROQ_API_KEY)
    audio_file =open(audio_filepath,"rb")
    transcription = client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return (transcription.text)
