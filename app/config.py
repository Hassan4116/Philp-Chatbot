import os 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("GROP_API_KEY")
