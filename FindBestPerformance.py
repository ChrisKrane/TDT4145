import sqlite3

def FindBestPerformance(): 
    try: 
        conn = sqlite3.connect('Theater.db')
        c = conn.cursor()
        c.execute(f'''SELECT Play.PlayName AS Play,
                             Performance.Date AS Date,
                             COUNT(Ticket.TicketID) AS Sold_seats
                      FROM Play JOIN Performance ON Play.PlayID = Performance.PlayID
                                JOIN Ticket ON Performance.PerformanceID = Ticket.PerformanceID
                      GROUP BY Play.PlayName, Performance.Date
                      ORDER BY Sold_seats DESC;''')
        result = c.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'An error occured {e}') 
    finally: 
        conn.close()


