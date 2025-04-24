import sqlite3

#path to the database
DATABASE = "database.db" 
con = sqlite3.connect(DATABASE)

#a cursor allows us to mess with the db
cur = con.cursor() 


