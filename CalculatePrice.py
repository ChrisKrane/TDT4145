import sqlite3

def calculatePrice(ticketID):
    price = 0
    try:
        connection = sqlite3.connect('Theater.db')
        cursor = connection.cursor()

        # Find the price of a ticket wit the given ticketID
        cursor.execute(
            "SELECT Price FROM Ticket WHERE TicketID = ?", (ticketID,)
        )
        result = cursor.fetchone()
        if result:
            price = result[0]
        else:
            print(f"No ticket found with TicketID: {ticketID}")
    except sqlite3.Error as msg:
        print("An error occurred: ", msg)
    finally:
        connection.close()

    return price