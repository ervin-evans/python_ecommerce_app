from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    JTW_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
