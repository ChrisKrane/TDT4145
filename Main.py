from Python_Files.Theater import createDatabase
from Python_Files.InitializeTheater import initializeDatabase
from Python_Files.InputSeats import motherLode
from Python_Files.BookTickets import bookTickets
from Python_Files.FindPlayOnDate import findPlayOnDate
from Python_Files.FindActor import findActor
from Python_Files.FindBestPerformance import findBestPerformance
from Python_Files.FindCoActors import findCoActors
import sqlite3

#This is the script that runs the program
def main():
    print("--------------------")
    print("Welcome to the Theater Database")
    print("Use '-help' for a list of commands")
    
    while input != "-q":
        print("--------------------")
        choice = input("Enter command: ")

        if choice == "-init":
            try:
                createDatabase()
                print("Database created successfully")
            except sqlite3.Error as msg:
                print("An error occurred: ", msg)

        elif choice == "-1":
            print("Filling database with sample data, this may take a short while...")
            try:
                initializeDatabase()
                print("Database filled successfully")
            except sqlite3.Error as msg:
                print("An error occurred: ", msg)

        elif choice == "-2":
            print("Filling database with occupied/unoccupied seats...")
            motherLode()
            print("Database filled successfully")

        elif choice == "-3":
            print("Booking tickets...")
            print("Your total price is: ", str(bookTickets()) + ",-")

        elif choice == "-4":
            print("Please write date in the format YYYY-MM-DD:")
            date = input("Enter date: ")
            print("Finding play and sale numbers on date...")
            formatPlayOnDate(findPlayOnDate(date))

        elif choice == "-5":
            print("Finding actors, play and role...")
            formatActor(findActor())

        elif choice == "-6":
            print("Finding best selling performances...")
            formatBestPerformance(findBestPerformance())

        elif choice == "-7":
            print("Please write actor name wihtout æ, ø or å. \næ => ae \nø => o \nå => aa")
            actor = input("Enter actor name: ")
            print("Finding co actors...")
            formatCoActors(findCoActors(actor))

        elif choice == "-help":
            help()
        elif choice == "-q":
            print("Goodbye!")
            break
        else:
            print("Invalid input, try again")

#Help commands
def help():
    print("'-init' : Create a new database. This will initiate a new database with empty tables.\nThis is intended for use to start over.")
    print("'-1' : Task 1: Fill a database with sample data.")
    print("'-2' : Task 2: Fill a database with occupied/unoccupied seats.")
    print("'-3' : Task 3: Book tickets.")
    print("'-4' : Task 4: Find play on date.")
    print("'-5' : Task 5: Find actor, their roles and the play they play in.")
    print("'-6' : Task 6: Find best selling performances.")
    print("'-7' : Task 7: Find co-actors in the same acts as where the given actor has played,\nand in which play the act is.")
    print("'-q' : Exit")
    print("'-help' : for a list of commands")

def formatPlayOnDate(input):
    for element in input:
        print(f"Play: {element[0]}, Seats sold: {element[1]}")

def formatActor(input):
    for element in input:
        print(f"Play: {element[0]}, Actor: {element[1]}, Role: {element[2]}")

def formatBestPerformance(input):
    count = 0
    for element in input:
        count += 1
        print(f"{count}. | Play: {element[0]}, Date: {element[1]}, Sold tickets: {element[2]}")

def formatCoActors(input):
    for element in input:
        if element[0] != element[1]:
            print(f"Co-actor: {element[1]}, Act: {element[3]}, Play: {element[2]}")


main()
