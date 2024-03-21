import sqlite3

#Takes an actor name in and finds all co actors performing in the same acts as the input actor. 
#Returns name of co actor, which act they play together in and the name of the play
# (Solves use case 7)
def findCoActors(ActorName):  
    try: 
        conn = sqlite3.connect('./Theater.db')
        c = conn.cursor()
        c.execute('''SELECT DISTINCT Actor1.Name AS Actor1, Actor2.Name AS Actor2, Play.PlayName AS PlayName, Act.Number AS ActNumber
                FROM Actor Actor1
                JOIN PlaysInRole PlaysInRole1 ON Actor1.ActorID = PlaysInRole1.ActorID
                JOIN Role Role1 ON PlaysInRole1.RoleID = Role1.RoleID
                JOIN RoleInAct RoleInAct1 ON Role1.RoleID = RoleInAct1.RoleID
                JOIN Act ON RoleInAct1.PlayID = Act.PlayID AND RoleInAct1.Number = Act.Number
                JOIN RoleInAct RoleInAct2 ON Act.PlayID = RoleInAct2.PlayID AND Act.Number = RoleInAct2.Number
                JOIN Role Role2 ON RoleInAct2.RoleID = Role2.RoleID
                JOIN PlaysInRole PlaysInRole2 ON Role2.RoleID = PlaysInRole2.RoleID
                JOIN Actor Actor2 ON PlaysInRole2.ActorID = Actor2.ActorID
                JOIN Play ON Act.PlayID = Play.PlayID
                WHERE Actor1.Name = ?''', (ActorName,))
        result = c.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'An error occured {e}') 
    finally: 
        conn.close()
        