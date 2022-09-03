import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__) / '.env')

def getenv(key):
    return os.getenv(key)
