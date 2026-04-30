
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
    

    def add_user(email, name):
        try:
            db = get_db_connection()
    
            cursor = db.cursor()
    
            sql = "INSERT INTO users (email) VALUES (%s)"
    
            values = (email, name)
    
            cursor.execute(sql, values)
    
            db.commit()
    
            cursor.close()
            db.close()
    
            return True
    
        except Exception as e:
            print("Error:", e)
            return False