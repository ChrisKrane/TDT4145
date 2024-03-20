import sqlite3

def initializeDatabase():
    try:
        connection = sqlite3.connect("Theater.db")
        cursor = connection.cursor()

        with open("Insertion.sql", "r") as sqlFile:
            sqlAsAString = sqlFile.read()

        cursor.executescript(sqlAsAString)
        connection.commit()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()