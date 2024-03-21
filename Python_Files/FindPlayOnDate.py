import sqlite3

#Finds, with the help of a SQL-query, which plays on a given date that is available. 
#It returns the name of the play and sold seats on the given performance
#(Solves use case 4)
def findPlayOnDate(date): 
    try: 
        conn = sqlite3.connect('./Theater.db')
        c = conn.cursor()
        c.execute(f'''SELECT Play.PlayName, COUNT(Ticket.TicketID) AS Sold_seats
                    FROM Play LEFT JOIN Performance ON Play.PlayID = Performance.PlayID
                              LEFT JOIN Ticket ON Performance.PerformanceID = Ticket.PerformanceID
                    WHERE Performance.Date = ?
                    GROUP BY Play.PlayID
                    ORDER BY Play.PlayName''', (date,))
        result = c.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'An error occured {e}') 
    finally: 
        conn.close()


    
