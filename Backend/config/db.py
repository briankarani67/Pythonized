# import mysql.connector

# def get_db_connection():
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="@Karani884",
#         database="testing",
#         SECRET_KEY="mysecretkey123"
#     )

#     return db

import mysql.connector
import os

from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)


def get_db_connection():

    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return db