from dotenv import load_dotenv     #acces throgh api and save api key
import os
import agents from A


load_dotenv()
gemini_api_key =os.getenv("GEMINI_API_KEY")