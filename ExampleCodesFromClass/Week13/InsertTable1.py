import sqlite3,os

dirpath = "/home/bangaru/PycharmProjects/516Spring18/Week13/commoncoredata/data"
filenames = os.listdir(dirpath)
conn = sqlite3.connect('5aprexercise2.sqlite')
cur = conn.cursor()

for filename in filenames:
    print(filename)
    full_file_path = os.path.join(dirpath,filename)
    #alternative: full_file_path = dirpath + "/" + file (those slashses will be different in windows!)
    print(full_file_path)
    content =  open(full_file_path, encoding="utf-8").read()
    cur.execute('INSERT INTO filecontents VALUES (?,?)',[filename,content])

conn.commit()
conn.close()




