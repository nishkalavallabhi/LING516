'''
Dec 23, 2016: Stephanie Fuccio
Purpose: This program marks the TRUE and FALSE answers from Response DB table and adds 0's and 1's for these answers in the Markings DB table. It sums the total marks (automatic and manually inputted marks) in the Markings DB table also.

This program is meant to be run AFTER the user has completed the test, i.e. after all the answers are in the Responses DB table.
'''
import sqlite3
con = sqlite3.connect('NewTextReader.sqlite')
cur=con.cursor()

def userans():# GETS user RESPONSES for all rows in Responses DB table
    cur.execute("SELECT ID,Textname,LitQ1Ans,ReorgQ1Ans,InfQ1Ans FROM Responses")
    userresp=cur.fetchall()
    return userresp

def startrow(): #ADDS IDs (only IDs) to MARKING DB TABLE to avoid DUPLICATE input
    responseinfo=userans() #pulls info from previous function
    #------------------IDs from Responses table-----------------------------#
    responseIDlist=[]
    for i in responseinfo:
        ID=(i[0])
        responseIDlist.append(ID)
    #------------------------IDs from Markings table-------------------------#
    cur.execute("SELECT ID FROM Markings")
    markingsID=cur.fetchall()
    markingsIDlist=[]
    for i in markingsID:
        ID=(i[0])
        markingsIDlist.append(ID)
    #-------------Compare IDs from two tables (searching for dups) ------------------#
    for i in responseIDlist:
        if i in markingsIDlist: #if a duplicate...
            pass #skip
        else:
            cur.execute('INSERT INTO Markings (ID) VALUES (?)', [i])
            con.commit()

def correctans():
    userresp=userans()
    resplist=[]
    #--------------------User Response List---------------------#
    for i in range (len(userresp)): #userresp IS a LIST
        rowid  = userresp[i][0] #unique row ID
        textname=userresp[i][1] #textname
        TFresp=userresp[i][2:] #3 T/F responses
        TFresp2=list(TFresp) #turn tuple into a list
        TFresp2.append(textname) #adds textname to the list
        TFresp2.append(rowid) #adds row id to the list
        resplist.append(TFresp2)
    #-----------------CORRECT ANSWER LIST -----------------#
    correctlist = []
    for i in range(len(resplist)): #collects correct answers from Questions DB table,based on textname from userinfo list textnames
        textname=(resplist[i][3])
        cur.execute("SELECT LitQ1correct,ReorgQ1correct, InfQ1correct FROM Questions WHERE TextName='" + resplist[i][3]+ "'")
        correctans = cur.fetchone()  # a LIST of tuples
        correctans2=list(correctans) #change from tuple to list
        correctans2.append(textname) #add text name
        correctlist.append(correctans2)
    #COMPARE RESPONSE LIST TO CORRECT LIST & MAKES LIST OF MARKS (0'1 and 1's)
    marklist=[]
    for i in range(len(resplist)):
        #--------------------------LIT Q1  Marking------------------#
        if resplist[i][0]==correctlist[i][0]:
            correct=(1)
            marklist.append(correct)
        else:
            incorrect=(0)
            marklist.append(incorrect)
        #-----------------------Reorg Q1  Marking-------------------#
        if resplist[i][1]==correctlist[i][1]:
            correct=(1)
            marklist.append(correct)
        else:
            incorrect=(0)
            marklist.append(incorrect)
        #------------------------Inf Q1  Marking-------------------#
        if resplist[i][2]==correctlist[i][2]:
            correct=(1)
            marklist.append(correct)
            marklist.append(resplist[i][3]) #textname
            marklist.append(resplist[i][4]) #ID
        else:
            incorrect=(0)
            marklist.append(incorrect)
            marklist.append(resplist[i][3]) #textname
            marklist.append(resplist[i][4]) #ID
    i=0
    allmarks=[]
    while i<len(marklist):
        A=(marklist[i:i+5])
        allmarks.append(A)
        i+=5
    return allmarks

def markstoDB(): #TRANSFERS textname & 3 T/F marks to Markings DB table for all rows (based on unique ID)
    markinginfo=correctans()
    for i in range(len(markinginfo)):
        LitQ1mark=(str(markinginfo[i][0]))
        ReorgQ1mark=(str(markinginfo[i][1]))
        InfQ1mark=(str(markinginfo[i][2]))
        textname=(markinginfo[i][3])
        ID=(str(markinginfo[i][4]))
        con.execute("UPDATE Markings SET Textname="+'"'+textname+'", '+"LitQ1Mark= " +'"'+ LitQ1mark+'",'+"ReorgQ1Mark= " +'"' + ReorgQ1mark+'",'+"InfQ1Mark= " +'"' + InfQ1mark  + '"'" WHERE ID= "+'"' +ID+'"')
    con.commit()

def totalmarks(): #TOTALS marks for all 6 columns (3 automatic via above code AND 3 manually entered)
    cur.execute("SELECT ID,LitQ1Mark,LitQ2Mark,ReorgQ1Mark,ReorgQ2Mark, InfQ1Mark,InfQ2Mark FROM Markings")
    rows=cur.fetchall()
    for i in rows:
        ID=(str(i[0]))
        total=sum(i[1:])
        total2=str(total)
        M=(total2)
        con.execute("UPDATE Markings SET TotalMarks="+'"'+M+'"'" WHERE ID= "+'"' +ID+'"')
        con.commit()
def main():
   userans()
   correctans()
   startrow()
   markstoDB()
   totalmarks()
   con.close()
if __name__ == "__main__":
    main()
