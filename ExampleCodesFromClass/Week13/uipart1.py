from bottle import get, post, request, route, run
import sqlite3

conn = sqlite3.connect('5aprexercise.sqlite')
cur = conn.cursor()

@route('/')
def home():
        return '''
        <form action="/filenamecheck" method="post">
            What is the file name?: <input name="filename" type="text" />
         <input value="submit" type="submit" />
        </form>
    '''

@post('/filenamecheck')  # or @route('/filenamecheck', method='POST')
def wherecheckinghappens():
    filename = request.forms.get('filename')
    cur.execute("SELECT filename,content from filecontents WHERE filename="+"'"+filename+"'")
    row_i_need = cur.fetchone()
    if row_i_need:
        print(row_i_need)
        return("Here are contents of:", row_i_need[0], "<br><br><br>", row_i_need[1])
    else:
        return("This file does not exist in my database")

@route('/2')
def sophisticatedhome():
        cur.execute("SELECT filename from filecontents")
        names = cur.fetchall()
        my_string = ""
        for name in names:
            my_string += name[0] + "<br>"
        return my_string + "<br><br><br>" +'''
        <form action="/filenamecheck" method="post">
            Type a file name from these: <input name="filename" type="text" />
         <input value="submit" type="submit" />

        </form>
    '''

#More sophistication: Make it look visually appealing, make users "select" instead of copy paste, etc.

run(reloader=True)
