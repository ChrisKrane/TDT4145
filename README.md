# File Structure and Recipe
Hello and welcome to our theater database. This is a recipe for how our program should be executed, as well as an overview of the files we use.

### Overview of Files:
- Theater.db: This is the empty database file that receives data when the program is executed.
- Theater.sql: This is the SQL file that creates all the tables in our database.
- Insertion.sql: This is the SQL file that inserts data provided in the assignment.
- Main.py: Python file that runs the program in the terminal.
- InitializeTheater.py: Python file that reads "Insertion.sql" and feeds the data into "Theater.db". This is the file that solves use case 1.
- InputSeats.py: Python file that reads the provided auxiliary files in the assignment, "gamle-scene.txt" and "hovedscenen.txt". Using these, the file inserts the seats into the database. Additionally, this file adds occupied seats on a given date in the auxiliary files (use case 2). The default user responsible for purchasing the occupied seats is also created in this file.
- FindSeats.py: Solves use case 3. It finds 9 available seats in the same row and returns the sum of what these tickets cost.
FindPlayOnDate.py: Solves use case 4 where a date is input and returns which performances are playing and the number of tickets sold on that date.
- FindActor.py: Solves use case 5. This was supposed to be just an SQL file, but since we have chosen to solve the program so that everything runs in the terminal, we have created a Python script for this as well.
- FindBestPerformance.py: Solves use case 6. The function finds which performances have sold the most tickets, where the number of tickets sold is sorted in descending order. This should also be just an SQL file, but we have chosen to solve this in the same way as the previous task because it is to be run in the terminal.
- FindCoActors.py: Solves use case 7. Takes in an actor's name and returns the name of the co-actor, which act, and which play this occurred in.

### Recipe for Using the Program
1. Open "Main.py".
2. Run the program and follow the instructions provided in the terminal:)

