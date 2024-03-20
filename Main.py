from Theater import createDatabase
from InitializeTheater import initializeDatabase
from InputSeats import motherLode
import sqlite3

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
        elif choice == "-fill":
            print("Filling database with sample data, this may take a short while...")
            try:
                initializeDatabase()
                motherLode()
                print("Database filled successfully")
            except sqlite3.Error as msg:
                print("An error occurred: ", msg)
        elif choice == "-open":
            #openDatabase()
            print("Not implemented yet")
        elif choice == "-help":
            help()
        elif choice == "-q":
            print("Goodbye!")
            break
        else:
            print("Invalid input, try again")

def help():
    print("'-init' : Create a new database")
    print("'-fill' : Fill a database with sample data")
    print("'-open' : Open an existing database")
    print("'-q' : Exit")
    print("'-help' : for a list of commands")

main()
