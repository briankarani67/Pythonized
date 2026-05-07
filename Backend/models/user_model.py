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


def add_user(name, email, password):

    try:
        db = get_db_connection()

        cursor = db.cursor()

        sql = """
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s)
        """

        values = (name, email, password)

        cursor.execute(sql, values)

        db.commit()

        cursor.close()
        db.close()

        return True

    except Exception as e:
        print("Error:", e)
        return False