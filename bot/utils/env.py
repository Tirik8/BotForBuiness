import os, sys
from dotenv import load_dotenv

def load_env():
    try:
        os.environ['BOT_API_KEY'] = sys.argv[1]
    except:
        dotenv_path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        else:
            raise FileNotFoundError(dotenv_path)