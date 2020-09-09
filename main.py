import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.join(BASE_DIR, ".env")
# load environment variable from .env
load_dotenv(dotenv_path=ENV)


AUTH_FIREBASE = os.getenv("AUTH_FIREBASE") 
FIRESTORE_URL = os.getenv("FIRESTORE_URL")

databaseURL = {
    'databaseURL': FIRESTORE_URL
}
cred = credentials.Certificate(AUTH_FIREBASE)
firebase_admin.initialize_app(cred, databaseURL)

database = firestore.client()