import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():

    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    print("HOST:", host)
    print("DATABASE:", database)

    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return db