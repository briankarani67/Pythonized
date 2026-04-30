
from config.db import get_db_connection

def get_all_users():
    try:
        db = get_db_connection()

        print("DATABASE:", db.database)

        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users")

        result = cursor.fetchall()

        print("RESULT:", result)

        cursor.close()
        db.close()

        return result

    except Exception as e:
        print("Error:", e)
        return []