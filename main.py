# Create .env file with API key

import os
import requests
import json
import berserk
import sqlite3
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session


con = sqlite3.connect("dcc.db")
cursor = con.cursor()

#cursor.execute('''CREATE TABLE IF NOT EXISTS Tournaments(
#                  USERNAME TEXT(34),
#                  POINTS INT(),
#                  TOURNAMENTS PLAYED INT(),
#                  TOURNAMENTS WON INT(),
#                  MATCHES PLAYED INT(),
#                  WON INT(),
#                  LOST INT(),
#                  DRAW INT(),
#                  BYES INT(),
#
#)''')


load_dotenv(override=True) 

API_TOKEN = os.getenv("API_KEY")
session = berserk.TokenSession(API_TOKEN) #type:ignore 
client = berserk.Client(session=session)

def pull_members(team):
    pass

def pull_games(user_list):
    pass

def pull_tournaments():
    pass

