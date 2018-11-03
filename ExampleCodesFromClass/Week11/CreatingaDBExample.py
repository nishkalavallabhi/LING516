import sqlite3


def createDatabase():
    conn = sqlite3.connect('isudb2.sqlite3')
    #.connect() method makes a connection to the .sqllite3 database on the hard-disk,
    #  in the filepath there.
    #if there is no such file, it will be created.
    #it is called connect, because we can also connect to some external server like this.

    cur = conn.cursor()
    #a cursor is like a "handle" for databases.
    #so conn.cursor() is similar to a .open() method in files.

    #once the cursor is defined, we can use it to access the database tables.
    cur.execute('DROP TABLE IF EXISTS ISUPeople')
    #this line above deletes the table ISUPeople if it already exists, and
    # allows us to create the table
    #again and again. It is not what we want to do if we don't want to lose our data though!

    cur.execute('CREATE TABLE ISUPeople (ISUID Integer, firstName STRING, '
                'lastName STRING, role STRING, email STRING)')
    #this command above creates a table inside our database, called ISUPeople,
    # and with five columns.

    conn.commit() #This line is important if you want your database to actually change!
    conn.close() #Always close the connection after you are done.

createDatabase()
