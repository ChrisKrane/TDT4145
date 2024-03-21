from FindSeats import findSeats
from NewTicket import newTicket
from NewCostumerProfile import newCostumerProfile
from CalculatePrice import calculatePrice

def bookTickets():
    # Creates a new costumer profile
    newCostumerProfile("Trond Teatersønn", "12345678", "Forestillingsalleen 13")
    # Finds the first available seats
    freeSeats = findSeats()
    ticketIDs = []

    for i in range(len(freeSeats)):
        seatNumber = freeSeats[i][0]
        rowNumber = freeSeats[i][1]
        area = freeSeats[i][2]

        ticketIDs.append(newTicket("2024-01-04", "13:41", seatNumber, rowNumber, area))

    # Calculate the total price of the tickets
    totalPrice = 0
    for i in range(len(ticketIDs)):
        ticketID = ticketIDs[i]
        price = calculatePrice(ticketID)
        totalPrice += price
    
    return totalPrice