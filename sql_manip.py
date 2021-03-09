import os
import sqlite3

# This class is a simplified form of a class from another one of my projects, it does what is necessary

class database:
    def __init__(self):# Initialize all variables required aswell as start connection to database
        self.name = 'storage'
        #check if databases folder exists, if it does not create it.
        try: os.makedirs('databases/')
        except: print('databases folder exists')
        self.dir = 'databases/'+self.name+'.db'
        # Create db
        self.conn = sqlite3.connect(self.dir) # connect to database
        self.conn.commit()
        self.c = self.conn.cursor()

    def __repr__(self):
        return f'<SQLite database : name = {self.name}, dir = {self.dir}, backup_dir = {self.backup_dir}>'

    def add_user(self, username, passwd): # Inserts username and passwd into the database. 
        self.c.execute('INSERT INTO passwds (name, pass) VALUES ( "{}", "{}" )'.format(username, passwd))
        self.conn.commit()
        return f'Added {username}, {passwd} to {self.name}'

    def get(self, username): # Returns the passwd from a username
        self.c.execute('SELECT pass FROM passwds WHERE name = "{}"'.format(username))
        passwd = self.c.fetchall()
        return passwd

    def get_names(self): # returns all names found within the database.
        self.c.execute('SELECT name FROM passwds')
        names = self.c.fetchall()
        return names
