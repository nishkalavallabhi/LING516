'''
Nov 27th: Stephanie
Purpose: This page will have the main code for the test (the one-time codes are in files 2_ and 3_)

Two potential issues needing attention:
1. Browser back button: not sure how to disable it for first round of questions. Found some info below but unable to get it working.
    http://stackoverflow.com/questions/12381563/how-to-stop-browser-back-button-using-javascript
    https://www.irt.org/script/311.htm
    http://stackoverflow.com/questions/12381563/how-to-stop-browser-back-button-using-javascript

2. Screenfit issue:(need to test it out on Linguistics Lab computers but pretty sure there is too much white space on the screen.)
    https://answers.yahoo.com/question/index?qid=20111119182536AABUvP3
    http://stackoverflow.com/questions/22911043/html-css-to-fit-all-screen-resolution
    http://stackoverflow.com/questions/19201715/how-do-i-get-a-page-to-auto-fit-to-a-window
'''
import bottle,sqlite3, string, random, uuid, sys,os, re
from bottle import get, post, request, route, redirect, run, template, static_file
from random import randint
import pprint
from urllib.request import urlopen
from datetime import datetime
import time, math

con = sqlite3.connect('For516on22ndMarch.sqlite')
cur=con.cursor()
usernameglobal = "" #figuring out ways to avoid this.
userreadings = {} #contains username as key, readings list (sixreadings[]) as value.
usertextnamelist = {} #contains username as key, textnamelist (textnamelist) as value.
questions=[] #global list of 6 questions for each text-DELETE?
qsdict={} #combines 6 textnames with their 6 questions (textnamelist + questions list)-not done yet
usercounter = {}

###----------------------------- PREPARES 6 READINGS AND ALL OF THEIR QUESTIONS --------------------------------------###

def readings(username):#makes a list of 6 random reading texts @ diff levels
    sixreadings = []
    cur.execute("SELECT DISTINCT TextName FROM TextTable ORDER BY RANDOM() LIMIT 6")
    titles = cur.fetchall()
    for item in titles:
        if username in usertextnamelist.keys():
            usertextnamelist[username].append(item[0])
        else:
            usertextnamelist[username] = []
            usertextnamelist[username].append(item[0])
    levellist=["Elem", "Int", "Adv","Elem", "Int", "Adv"]
    tup1 = usertextnamelist[username]
    tup2 = levellist
    for i in range(6):
        cur.execute("SELECT Content FROM TextTable WHERE TextName = '" + tup1[i] + "' AND ReadingLevel = '" + tup2[i] + "'")
        text=cur.fetchone()[0]
        sixreadings.append([text,tup1[i],tup2[i]])#sixreadings   =   [content,name,RL], a very long thing!
    qdict(username)
    userreadings[username] = sixreadings #print("line 57, what is user readings, include RL?",userreadings)#full texts:(
    return userreadings

def qdict(username):
    global qsdict #{KEYS,VALUES}; the merge of these 2 lists will go to this dict
    global questions
    i=0
    while i <len(usertextnamelist[username]):
        cur.execute("SELECT  LitQ1, LitQ2, ReorgQ1, ReorgQ2, InfQ1, InfQ2 FROM Questions WHERE TextName = '" +usertextnamelist[username][i]+ "'")
        qs=cur.fetchone() #retrieves the 6 questions from DB
        questions.append(list(qs)) #and adds them to this list as VALUES
        k=usertextnamelist[username][i] #KEY for each iteration
        v=list(qs) #VALUE for each iteration
        i+=1 #iterate initiater
        qsdict[k]=v #adds above KEY(textname) and its six VALUES (the questions) into QSDICT dictionary

            ###------------------------------------- STARTS READING TEST --------------------------------------###
@route('/')
def intro():
    page = open("a_intro.html")
    text = page.read()
    return(text)

@get('/login',method="get")
def login():
    page = open("b_login.html")
    text = page.read()
    return text

@post('/userdetails')
def userdetails(): #checks input username AND password with UserLogin DB username and password
    username = request.forms.get('username')
    password = request.forms.get('password')
    cur.execute("SELECT Username,Password FROM UserLogin WHERE Username='"+username+"'") #matches input username with DB username, gets DB password
    loginsrow = cur.fetchone() #loginsrow=DB username, password, a tuple ('user3', 'ivsfhr')
    if loginsrow is not None: #if DB info is not empty...
        Username, Password = loginsrow #...DB Username + DB Password=loginsrow
        if password == Password: #IF input password =DB password, go to UserDetails page
            if sameasDBcheck(username)==True: #if input password matches UserLogin password BUT someone already used this username
                return "This username has already been used. Please tell inform the test administrator about this now."
            else: #BUT if no one has logged in with this info yet...
                readings(username) #...create readings AND questions list ...
                print("line 99,Text titles for ", username, "are: ", str(usertextnamelist[username]))
                return template('c_userdetails.tpl',username=username) #...and open next page (UserDetails)
        else:
            return "This password is incorrect. Please try again."

def sameasDBcheck(username): #Checks for username duplicates in UserDetails DB table using login input info
    cur.execute("SELECT Username FROM UserDetails WHERE Username='"+username+"'") #matches input username with DB username, gets DB password
    for item in cur:#if the name being transferred is already in th DB...
        return True #...tell the program TRUE
    return False #If the name is not already in DB, tell program FALSE
    #true/false used in userdetails()

@post('/readingonly') #moves user details to DB, opens first reading page
def bigloop():
    global usernameglobal
    username = request.forms.get('username')
    if not username in usercounter.keys():
        usercounter[username] = 0
        L1 = request.forms.get('L1').replace("\"","'")
        YearsofEnglish = request.forms.get('YearsofEnglish').replace("\"","'")
        Otherdetails=request.forms.get('Otherdetails').replace("\"","'")
        cur.execute('INSERT INTO UserDetails (Username,L1,YearsofEnglish,Otherdetails) VALUES (?,?,?,?) ', [username,L1, YearsofEnglish, Otherdetails])
        con.commit()
    ###------------------------------------- STARTS SIX TEXT LOOP --------------------------------------###
    #textname and counter have parallel numbers the entire reading test.
    text1=usertextnamelist[username][0]
    text2=usertextnamelist[username][1]
    text3=usertextnamelist[username][2]
    text4=usertextnamelist[username][3]
    text5=usertextnamelist[username][4]
    text6=usertextnamelist[username][5]
    if usercounter[username] <=5:
        Textname=usertextnamelist[username][usercounter[username]]
        return template('d_readingonly.tpl', rows=userreadings[username][usercounter[username]], username =username,text1=text1, text2=text2, text3=text3,text4=text4,text5=text5,text6=text6,textname=Textname) #sixreadings[counter] = all text info for ONE iteration text
    else:
        usernameglobal = username
        redirect('/proftest')

@post('/litqa')
def timetime():
    username = request.forms.get('username')
    global questions
    global qsdict
    Textname=usertextnamelist[username][usercounter[username]] #current text name only
    Q1=qsdict[Textname][0]
    Q2=qsdict[Textname][1]
    levellist=["Elem", "Int", "Adv","Elem", "Int", "Adv"] #everey test has same level order so, use indexing here
    TextCounter=usertextnamelist[username].index(Textname)
    #TIME NOTES: 1 minute in DB=1, 1 minute 33 seconds in DB=1.55 (1 + 33/60=.55=1.55)
    timespent = request.forms.get('timespent')
    seconds = (int(timespent)/1000)
    minutes=(int(seconds)/60)
    totaltime=(round(minutes,2))
    cur.execute('INSERT INTO Responses(Username,Textname,ReadingLevel,TextCounter,ReadingOnlyTime) VALUES (?,?,?,?,?)',[username,Textname,levellist[TextCounter],TextCounter,totaltime])
    con.commit()
    #This is for the left nav menu in UI
    text1=usertextnamelist[username][0]
    text2=usertextnamelist[username][1]
    text3=usertextnamelist[username][2]
    text4=usertextnamelist[username][3]
    text5=usertextnamelist[username][4]
    text6=usertextnamelist[username][5]
    return template('e_litqa.tpl', row1=Q1,row2=Q2,username =username, rows=userreadings[username][usercounter[username]],textname=Textname,text1=text1, text2=text2, text3=text3,text4=text4,text5=text5,text6=text6) #row1=question1, row2=question2, rows=sixreadings[counter]=textname

@post('/reorgqa')
def q1q2(): #moves Q1 and Q2 to Responses DB Table
    Question1 = request.forms.get('LitQ1Ans').replace("\"","'")
    Question2 = request.forms.get('LitQ2Ans').replace("\"","'")
    username = request.forms.get('username')
    global qsdict
    Textname=usertextnamelist[username][usercounter[username]]
    Q3=qsdict[Textname][2]
    Q4=qsdict[Textname][3]
    #This is for the left nav menu in UI
    text1=usertextnamelist[username][0]
    text2=usertextnamelist[username][1]
    text3=usertextnamelist[username][2]
    text4=usertextnamelist[username][3]
    text5=usertextnamelist[username][4]
    text6=usertextnamelist[username][5]
    cur.execute("UPDATE Responses SET LitQ1Ans=" + '"' + Question1+ '", ' + "LitQ2Ans=" + '"' + Question2 + '"'" WHERE Username = " + '"' +username + '"' + " AND Textname = " + '"' + Textname + '"')
    con.commit()
    return template('f_reorgqa.tpl',row3=Q3,row4=Q4,rows=userreadings[username][usercounter[username]], username =username,textname=Textname,text1=text1, text2=text2, text3=text3,text4=text4,text5=text5,text6=text6) #row3=question3, row4=question4

@post('/infqa')
def q3q4(): #moves Q3 and Q4 to Responses DB Table
    Question3 = request.forms.get('ReorgQ1Ans').replace("\"","'")
    Question4 = request.forms.get('ReorgQ2Ans').replace("\"","'")
    username = request.forms.get('username')
    global qsdict
    Textname=usertextnamelist[username][usercounter[username]]
    Q5=qsdict[Textname][4]
    Q6=qsdict[Textname][5]

    #This is for the left nav menu in UI
    text1=usertextnamelist[username][0]
    text2=usertextnamelist[username][1]
    text3=usertextnamelist[username][2]
    text4=usertextnamelist[username][3]
    text5=usertextnamelist[username][4]
    text6=usertextnamelist[username][5]
    cur.execute("UPDATE Responses SET ReorgQ1Ans=" + '"' + Question3+ '", ' + "ReorgQ2Ans=" + '"' + Question4 + '"'" WHERE Username = " + '"' + username + '"' + " AND Textname = " + '"' + Textname + '"')
    con.commit()
    return template('g_infqa.tpl',row5=Q5,row6=Q6,rows=userreadings[username][usercounter[username]], username =username,textname=Textname,text1=text1, text2=text2, text3=text3,text4=text4,text5=text5,text6=text6)

@post('/nexttext')
def q5q6(): #moves Q5 and Q6 to Responses DB Table AND counts how many readings its done so far
    username = request.forms.get('username')
    global textnamelist
    global counter
    Textname=usertextnamelist[username][usercounter[username]]
    Question5 = request.forms.get('InfQ1Ans').replace("\"","'")
    Question6 = request.forms.get('InfQ2Ans').replace("\"","'")
    cur.execute("UPDATE Responses SET InfQ1Ans=" + '"' + Question5+ '", ' + "InfQ2Ans=" + '"' + Question6 + '"'" WHERE Username = " + '"' +username + '"' + " AND Textname = " + '"' + Textname + '"')
    con.commit()
    usercounter[username] += 1
    return bigloop()

@route('/proftest')
#@get('/proftest')
def proftesttrial():
    global usernameglobal
    username = usernameglobal
    text1=usertextnamelist[username][0]
    text2=usertextnamelist[username][1]
    text3=usertextnamelist[username][2]
    text4=usertextnamelist[username][3]
    text5=usertextnamelist[username][4]
    text6=usertextnamelist[username][5]
    return template('h_proftest.tpl',username=username,text1=text1, text2=text2, text3=text3,text4=text4,text5=text5,text6=text6)

@post('/byepage')
def proftodb():#moves prof test info to Responses DB table THEN goes to bye/thanks page
    ProfTest = request.forms.get('ProfTest1')
    username = request.forms.get('username')
    cur.execute("UPDATE Responses SET ProfTest=" + '"' + ProfTest + '"'" WHERE Username = " + '"' +username + '"')
    con.commit()
    #con.close() #only once when the user is done with the entire test.
    page = open("i_byepage.tpl")
    text = page.read()
    return text

run(host='localhost', port=8083)
'''
Sowmya's reminder:
For the user data to come back to server, I should first commit the version on the experiment server into gitlab - otherwise it will be overwritten :o
run(host='10.24.227.243', port=80)
'''

