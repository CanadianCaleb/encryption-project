import encryption as enc
import sql_manip as sql

# Simple encryption progam with a bit of sql to store users and their encrypted passphrases.

db = sql.database()

def check_user(name, passwd): # Checks if user can be found within the database
    try: 
        if passwd == enc.decrypt(db.get(name)[0][0][1:].replace("'", '').encode()):
            return 'Password correct and name exists.'
        else:
            return 'Name exists, password incorrect.'
    except: 
        return 'Name does not exists.'

def add_user(name, password): # Adds user to database
    names = [str(i[0]) for i in db.get_names()]
    if name not in names:
        if name.isalnum() and password.isalnum():
            db.add_user(name, enc.encrypt(password))
            return 'user added'
        else:
            return 'invalid input'
    else:
        return 'user already exists'

def get(user): # Returns user fr0k database
    if user in names:
        return 'user : ' + user + '\npassword : ' + enc.decrypt(db.get(user)[0][0][1:].replace("'", '').encode())
    else:
        return 'user does not exist'

username = ''
while username != 'q' : # loop to allowe console commands
    names = [str(i[0]) for i in db.get_names()]
    code = str(input()).split(' ')
    if code[0] == 'get_all':
        print([str(i[0]) for i in db.get_names()])
    if code[0] == 'add':
        print(add_user(code[1], code[2]))
    elif code[0] == 'get':
        print(get(code[1]))
    elif code[0] == 'login':
        print(check_user(code[1], code[2]))
