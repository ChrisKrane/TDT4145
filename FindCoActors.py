import sqlite3

def FindCoActors(ActorName):  
    try: 
        conn = sqlite3.connect('Theater.db')
        c = conn.cursor()
        c.execute(f'''SELECT Actor.Name, Act.Number, Play.PlayName
                      FROM Actor INNER JOIN PlaysInRole ON Actor.ActorID = PlaysInRole.ActorID 
                                 INNER JOIN Role ON PlaysInRole.RoleID = Role.RoleID
                                 INNER JOIN RoleInAct ON Role.RoleID = RoleInAct.RoleID
                                 INNER JOIN Act ON RoleInAct.PlayID AND RoleInAct.Number = Act.PlayID AND Act.Number
                                 INNER JOIN Play ON Act.PlayID = Play.PlayID
                      WHERE Act.PlayID IN (
                                 SELECT Play.PlayID
                                 FROM Actor INNER JOIN PlaysInRole ON Actor.ActorID = PlaysInRole.ActorID
                                            INNER JOIN Role ON PlaysInRole.RoleID = Role.RoleID
                                            INNER JOIN RoleInAct ON Role.RoleID = RoleInAct.RoleID AND RoleInAct.PlayID = Role.PlayID
                                            INNER JOIN Act ON RoleInAct.PlayID = Act.PlayID AND RoleInAct.Number = Act.Number
                                            INNER JOIN Play ON Act.PlayID = Play.PlayID
                                 WHERE Actor.Name = ?) 
                      AND Act.Number IN (
                                 SELECT Act.Number
                                 FROM Actor INNER JOIN PlaysInRole ON Actor.ActorID = PlaysInRole.ActorID
                                            INNER JOIN Role ON PlaysInRole.RoleID = Role.RoleID
                                            INNER JOIN RoleInAct ON Role.RoleID = RoleInAct.RoleID AND RoleInAct.PlayID = Role.PlayID
                                            INNER JOIN Act ON RoleInAct.PlayID = Act.PlayID AND RoleInAct.Number = Act.Number
                                 WHERE Actor.Name = ?);''', (ActorName, ActorName,))
        result = c.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'An error occured {e}') 
    finally: 
        conn.close()

print(FindCoActors('Arturo Scotti'))