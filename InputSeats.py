import sqlite3
import re
from datetime import datetime

def readSeats(filename):
    with open(filename, "r") as seatFile:
        data = seatFile.read().strip()
    rows = data.split()
    if "Dato" in rows:
        for word in rows:
            if len(word) == 10 and word[4] == "-" and word[7] == "-":
                date =  word
    rows.pop(rows.index("Dato"))
    rows.pop(rows.index(date))

    pattern = re.compile(r'^[0-1x]+$')
    areas = []
    currentAreaDict = {}
    currentAreaName = ''
    currentAreaRows = []

    for element in rows:
        if not pattern.match(element):
            if currentAreaRows:
                currentAreaDict = {"Area": currentAreaName}
                for index, row in enumerate(reversed(currentAreaRows), start = 1):
                    currentAreaDict[index] = row
                areas.append(currentAreaDict)
            currentAreaName = element
            currentAreaRows = []
        else:
            currentAreaRows.append(element)

    if currentAreaRows:
        currentAreaDict = {"Area": currentAreaName}
        for index, row in enumerate(reversed(currentAreaRows), start = 1):
            currentAreaDict[index] = row
        areas.append(currentAreaDict)

    areas.reverse()

    return areas, date

def inputScene(filename):
    areas, date = readSeats(f"{filename}")
    try:
        connection = sqlite3.connect("Theater.db")
        cursor = connection.cursor()

        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        currentTime = currentTime[:5]

        if(filename == "files/hovedscenen.txt"):
            seatNumber = 0

        for area in areas:
            areaName = area["Area"]
            for row, seats in area.items():
                if row != "Area":
                    if(filename == "files/gamle-scene.txt"):
                        seatNumber = 0
                    rowNumber = row
                    for i in range(0, len(seats)):
                        available = True
                        if seats[i] == "x":
                            available = False
                        seatNumber += 1

                        cursor.execute(
                            "SELECT count(*) FROM Ticket"
                        )
                        ticketCountDB = cursor.fetchone()
                        ticketCount = ticketCountDB[0]
                        ticketID = ticketCount + 1

                        if(filename == "files/hovedscenen.txt"):
                            cursor.execute(
                                "INSERT INTO Seat (SeatNumber, RowNumber, Area, HallID, Available) VALUES (?, ?, ?, ?, ?)",
                                (seatNumber, rowNumber, areaName, 1, available)
                            )
                            if seats[i] == "1":
                                cursor.execute(
                                    "INSERT INTO Ticket (TicketID, Price, CostumerGroup, DateOfSale, TimeOfSale, PerformanceID, CostumerID, SeatNumber, RowNumber, Area, HallID ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                    (ticketID, 450, "Ordinary", date, currentTime, 3, 1, seatNumber, rowNumber, areaName, 1)
                                )
                            connection.commit()
                        if(filename == "files/gamle-scene.txt"):
                            cursor.execute(
                                "INSERT INTO Seat (SeatNumber, RowNumber, Area, HallID, Available) VALUES (?, ?, ?, ?, ?)",
                                (seatNumber, rowNumber, areaName, 2, available)
                            )
                            if seats[i] == "1":
                                cursor.execute(
                                    "INSERT INTO Ticket (TicketID, Price, CostumerGroup, DateOfSale, TimeOfSale, PerformanceID, CostumerID, SeatNumber, RowNumber, Area, HallID ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                    (ticketID, 450, "Ordinary", date, currentTime, 6, 1, seatNumber, rowNumber, areaName, 2)
                                )
                            connection.commit()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

def costumerProfile():
    try:
        connection = sqlite3.connect("Theater.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM CostumerProfile WHERE CostumerID = 1"
        )
        costumer = cursor.fetchone()

        if not costumer:
            cursor.execute(
                "INSERT INTO CostumerProfile (CostumerID, PhoneNumber, Name, Address) VALUES (?, ?, ?, ?)",
                (1, "12345678", "Ola Nordmann", "Teaterveien 1839, Trondheim")
            )
            connection.commit()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

def motherLode():

    costumerProfile()
    inputScene("files/hovedscenen.txt")
    inputScene("files/gamle-scene.txt")
