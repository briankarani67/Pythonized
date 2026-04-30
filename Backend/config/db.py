import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Karani884",
        database="testing"
    )

    print("CONNECTED TO:", db.database)

    return db