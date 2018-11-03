'''
Dec 20, 2016: Stephanie Fuccio
Purpose: Creates 150 userlogins and passwords, and saves them to the UserLogin DB table.
Usernames: User1...User150
Passwords: 6 character randomly generated strings
'''

import sqlite3, string, random, collections, re
con = sqlite3.connect('NewTextReader.sqlite')
cur=con.cursor()

#------------------------creates user logins & puts them into UserLogin DB table-----------------------------------#

def gen_random_string(): #generates a random 6 character string, to be used as password
    return ''.join(random.choice(string.ascii_lowercase) for x in range(6))

def create_id_password_pairs():#Creates 150 user name-password pairs
    upasswd = {}
    for i in range(150):
        userName = "user" + str(i+1)
        passWord = gen_random_string()
        upasswd[userName] = passWord
    return upasswd

def sorted_nicely(l):#sorts alpha-numeric strings
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

def fill_login_table():#populates the UserLogin DB table
    namepasswd = create_id_password_pairs()
    namesList = sorted_nicely(list(namepasswd.keys())) #gets numerically sorted key list
    for name in namesList:
        cur.execute('INSERT INTO UserLogin(UserName, Password) VALUES (?,?)', [name, namepasswd[name]])
    con.commit()
    con.close()

def main():

    fill_login_table()

if __name__ == '__main__':
  main()
