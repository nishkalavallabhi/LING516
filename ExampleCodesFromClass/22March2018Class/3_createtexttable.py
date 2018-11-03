'''
Dec 20,2016:Stephanie
Purpose: copies reading text info from folder to db table
NOTE: The Questions DB table was manually uploaded from CODE directory (Questions.csv file) into NewTextReader.sqlite DB
'''
import sqlite3, string, random, uuid, os, re
from urllib.request import urlopen
con = sqlite3.connect('NewTextReader.sqlite')
cur=con.cursor()

def texttable():
    for files in os.listdir("../texttable"):
        filepath = os.path.join("../texttable",files)
        if filepath.endswith(".txt"):
            text_name1= files.split(os.sep)[-1] #prints as Rats_Adv.txt (entire file name)
            text_name2 = re.sub(r'\_Elem|\_Int|\_Adv', '', text_name1) #prints Rats.txt (removes level)
            text_name3 = re.sub(r'\.txt$', '', text_name2) #prints Rats (just name w/o level or txt)

            RL1= files.split(os.sep)[-1] #prints Rats.Adv.txt
            RL2=RL1.replace('.txt','') #prints Rats.Adv (removes .txt)
            RL3 = RL2.replace('_', ':').split(':')[-1] #prints Adv (only RL)

            content1=open(filepath,"r")
            content2=(content1.read().replace(u'\ufeff',''))

            dict={"TextName": text_name3,"ReadingLevel":RL3,"Content": content2}

            for key in sorted(dict):
                print("%s: %s" % (key, dict[key]))
            cur.execute ('INSERT INTO Texttable(TextName, Content, ReadingLevel) VALUES(?,?,?)', [dict["TextName"], dict["Content"], dict["ReadingLevel"]])
            con.commit()
        else:
            print("There has been an error.")

def main():

    texttable()

if __name__ == "__main__":
    main()


