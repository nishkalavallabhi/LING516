import sqlite3

conn = sqlite3.connect('isudb.sqlite3')
cur = conn.cursor()

def printFromADB(cur):
    cur.execute("SELECT * FROM ISUPeople")
    #SELECT is used just to pick some (or all if it is a *) rows from database which match a condition.
    #we can use a for loop, to print each row contents as tuples.
    for item in cur:
        print(item)

def editAnItem(cur):
    cur.execute("UPDATE ISUPeople SET firstName='Andy2' WHERE "
                "firstName='Andy'")
    #UPDATE is used to change some row in a database based on some condition.
    #SET is used to give a new value to a cell in the table that satisfies some condition (WHERE)

def deleteAnItem(cur):
    cur.execute("DELETE from ISUPeople WHERE firstName = 'C'")
    #DELETE is the SQL command you use to delete rows. WHERE specifies the condition for deletion

printFromADB(cur)

#editAnItem(cur)
deleteAnItem(cur)
conn.commit()


print("********")
printFromADB(cur)

#conn.commit()
#conn.close()

'''
An important note, copied verbatim from textbook:
"Note, unlike in Python, in a SQL WHERE clause we use a single equal sign to indicate a test for equality
rather than a double equal sign. Other logical operations allowed in a WHERE clause include <, >, <=, >=, !=,
as well as AND and OR and parentheses to build your logical expressions."
'''
