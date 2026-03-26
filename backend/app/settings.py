import logging

# --- SERVER CONFIG ---
PORT = 5000
HOST = "127.0.0.1"
DEBUG = True
SECRET_KEY = "your-secret-key-here"
JWT_SECRET_KEY = "your-jwt-secret-key-here"

# --- DATABASE CONFIG ---
DB_NAME = "demo_2wnx"
DB_USER = "bomxanhgz"
DB_PASSWORD = "ECQ1zkugQRHyxNkWqRXxDWpuWGUnoYPN"
DB_HOST = "dpg-d72au55m5p6s73cu4d6g-a.oregon-postgres.render.com"
DB_PORT = "5432"
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# --- LOGGING CONFIG ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)
logger = logging.getLogger(__name__)

# --- PREFIX REGISTER ---
API_PREFIX = "/api"
