import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("BASE_URL", "https://openai.vocareum.com/v1")

def get_openai_client():
    return openai