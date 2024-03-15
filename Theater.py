import sqlite3

connection = sqlite3.connect("Theater.db")

def createDatabase():
    cursor = connection.cursor()

    # Separate the commands from the sql file
    sqlFile = open("Theater.sql", "r")
    sqlAsAString = sqlFile.read()
    sqlFile.close()

    sqlCommands = sqlAsAString.split(";")   # split the commands by semicolon

    ## Execute every command from the input file
    for command in sqlCommands:
        try:
            cursor.execute(command)
            connection.commit()
        except sqlite3.OperationalError as msg:
            print("Command skipped: ", msg)



connection.close()