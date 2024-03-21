import sqlite3

def findSeats():    
    connection = sqlite3.connect('Theater.db')
    cursor = connection.cursor()
    try:
        # Finds the number of unoccupied seats per row and area
        cursor.execute('''SELECT Seat.RowNumber, Seat.Area, COUNT(*) AS UnoccupiedSeats
            FROM Seat
            LEFT JOIN Ticket ON Seat.SeatNumber = Ticket.SeatNumber
                            AND Seat.RowNumber = Ticket.RowNumber
                            AND Seat.Area = Ticket.Area
                            AND Seat.HallID = Ticket.HallID
            WHERE Seat.HallID = 2 AND Ticket.TicketID IS NULL
            GROUP BY Seat.RowNumber, Seat.Area
            ORDER BY Seat.RowNumber, Seat.Area'''
            )
        seatInfo = cursor.fetchall()

        # Iterates through the rows
        for i in range(len(seatInfo)):
            availableSeats = []
            # Find a row with 9 or more unoccupied seats
            if seatInfo[i][2] >= 9:
                #Find the unoccupied seats in the row
                cursor.execute('''SELECT Seat.SeatNumber, Seat.RowNumber, Seat.Area, Seat.HallID
                    FROM Seat
                    LEFT JOIN Ticket ON Seat.SeatNumber = Ticket.SeatNumber
                                    AND Seat.RowNumber = Ticket.RowNumber
                                    AND Seat.Area = Ticket.Area
                                    AND Seat.HallID = Ticket.HallID
                    WHERE Seat.RowNumber = ? AND Seat.Area = ? AND Ticket.TicketID IS NULL AND Seat.HallID = 2'''
                    , (seatInfo[i][0], seatInfo[i][1]))
                rowInfo = cursor.fetchall()
                # Appends the 9 first unoccupied seats in the row to the availableSeats list
                for j in range(9):
                    availableSeats.append(rowInfo[j])
                break
    except sqlite3.Error as msg:
        print("An error occurred: ", msg)
    finally:
        connection.close()

    return availableSeats

findSeats()
