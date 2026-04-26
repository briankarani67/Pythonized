from config.db import get_db_connection

def get_all_users():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        cursor.close()
        db.close()
        return result

    except Exception as e:
            print("Error:", e)
            return []

