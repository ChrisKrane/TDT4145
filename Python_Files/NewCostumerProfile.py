import sqlite3

def newCostumerProfile(name, phone, address):
    
    try:
        connection = sqlite3.connect("./Theater.db")
        cursor = connection.cursor()

        # Find the number of costumer profiles in the database and add 1 to get the new CostumerProfileID
        cursor.execute(
            "SELECT COUNT(*) FROM CostumerProfile"
        )
        ID = cursor.fetchone()[0] + 1

        # Insert the new costumer profile into the database
        cursor.execute("INSERT INTO CostumerProfile (CostumerID, PhoneNumber, Name, Address) VALUES (?, ?, ?, ?)", 
                       (ID, phone, name, address))
        connection.commit()
        connection.close()
    except sqlite3.Error as msg:
        print("An error occurred: ", msg)