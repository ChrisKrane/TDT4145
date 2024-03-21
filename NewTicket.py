import sqlite3
from datetime import datetime

def newTicket(date, time, seatnumber, rownumber, area):

    costumerGroup = "Ordinary"
    ticketID = 0

    try:
        connection = sqlite3.connect('Theater.db')
        cursor = connection.cursor()

        # Find the performanceID and playID
        cursor.execute(
            "SELECT * FROM Performance WHERE Date = '2024-02-03' AND Time = '18:30'"
        )
        ticketInfo = cursor.fetchall()
        print(ticketInfo)
        performanceID = ticketInfo[0][0]
        playID = ticketInfo[0][3]

        # Find the hallID and price
        cursor.execute(
            "SELECT HallID, Ordinary FROM Play WHERE PlayID = ?",
            (playID,)
        )
        playInfo = cursor.fetchall()[0]
        hallID = playInfo[0]
        price = playInfo[1]

        # Find the number of tickets in the database and add 1 to get the new ticketID
        cursor.execute(
            "Select COUNT(*) FROM Ticket"
        )
        ticketID = cursor.fetchone()[0] + 1

        cursor.execute("INSERT INTO Ticket (TicketID, Price, CostumerGroup, DateOfSale, TimeOfSale, PerformanceID, CostumerID, SeatNumber, RowNumber, Area, HallID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                  (ticketID, price, costumerGroup, date, time, performanceID, 2, seatnumber, rownumber, area, hallID))
        connection.commit()

    except sqlite3.Error as msg:
        print("An error occurred: ", msg)
    finally:
        connection.close()

    # return ticketID to be used in calculating price
    return ticketID

