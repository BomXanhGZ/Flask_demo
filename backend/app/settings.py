import os
from datetime import timedelta
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# --- Server Configuration ---
PORT = int(os.getenv("PORT"))
HOST = os.getenv("HOST")
DEBUG = os.getenv("DEBUG") == "True"

# --- Database Configuration ---
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# --- API Routes ---
API_PREFIX = "/api"

# --- JWT Configuration ---
JWT_ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(
    minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))

# --- Google OAuth Configuration ---
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
