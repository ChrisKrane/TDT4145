import sqlite3

#Reads the "Insertion.sql" file and feeds data into the empty "Theater.db" database
def initializeDatabase():
    try:
        connection = sqlite3.connect("./Theater.db")
        cursor = connection.cursor()

        with open("./SQL_Files/Insertion.sql", "r") as sqlFile:
            sqlAsAString = sqlFile.read()

        cursor.executescript(sqlAsAString)
        connection.commit()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()