import sqlite3

def insertData():
    conn = sqlite3.connect('isudb2.sqlite3')
    cur = conn.cursor()
    #Let us insert some stuff into this database
    #INSERT is the command used in SQL to put new values into the database.
    cur.execute('INSERT INTO ISUPeople VALUES (1, "Sowmya","Vajjala","faculty","sowmya@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (2, "AA","BB","student","ab@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (3, "C","D","student","cd@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (4, "E","F","student","ef@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (5, "C","D","student","cd@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (6, "EE","FF","student","ef@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (7, "CC","DD","student","cd@iastate.edu")')
    cur.execute('INSERT INTO ISUPeople VALUES (8, "EEE","FFF","student","ef@iastate.edu")')

    conn.commit() #this line actually sends all your changes to the database. Don't forget this!
    conn.close() #close the connectiion

insertData()
