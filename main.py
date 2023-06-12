# Create .env file with API key

import os
import berserk
import sqlite3
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session

load_dotenv(override=True) 

API_TOKEN = os.getenv("API_KEY")
session = OAuth2Session(API_TOKEN)
client = berserk.Client(session)

