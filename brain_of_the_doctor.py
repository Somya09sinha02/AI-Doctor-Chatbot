import os
import base64
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key safely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in environment variables")

# Initialize Groq client ONCE
client = Groq(api_key=GROQ_API_KEY)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

query="is there something wrong with my face?"
model = "distil-whisper-large-v3-en"
def analyze_image_with_query(query, encoded_image, model):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content
