import os, sys
from dotenv import load_dotenv

def load_env():
    if sys.argv[1]:
        os.environ['BOT_API_KEY'] = sys.argv[1]
    else:
        dotenv_path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        else:
            raise FileNotFoundError(dotenv_path)