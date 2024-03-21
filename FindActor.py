import sqlite3

def FindActor(): 
    try: 
        conn = sqlite3.connect('Theater.db')
        c = conn.cursor()
        c.execute(f'''SELECT Play.PlayName AS Play,
                             Actor.Name AS Actor,
                             Role.Name AS Role
                      FROM Play JOIN Role ON Play.PlayID = Role.PlayID
                                JOIN PlaysInRole ON Role.RoleID = PlaysInRole.RoleID
                                JOIN Actor ON PlaysInRole.ActorID = Actor.ActorID''')
        result = c.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'An error occured {e}') 
    finally: 
        conn.close()

print(FindActor())
