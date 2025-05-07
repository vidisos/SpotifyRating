import sqlite3

#path to the database
DATABASE = "database.db" 

#creates tables if they dont exist
file_path = "src/sql/create_tables.sql"
with open(file_path) as file:
    con = sqlite3.connect(DATABASE) 
    #a cursor allows us to mess with the db
    cur = con.cursor()

    #reads the sql file as text and executes it
    cur.executescript(file.read())

    
#updated ish
def run_query(file_path: str, variables: dict) -> None:
    with open(file_path) as file:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute(file.read(), variables)
    
    
    