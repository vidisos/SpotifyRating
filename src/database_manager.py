import sqlite3

#path to the database
DATABASE = "database.db" 

#creates tables if they dont exist
file_path = "src/sql/create_tables.sql"
with open(file_path) as file: 
    #connects to the db and allows control with cursor
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()

    #reads the sql file as text and executes it
    cur.executescript(file.read())
    

def run_query(file_path: str, variables: dict) -> str:
    with open(file_path) as file:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute(file.read(), variables)

        return cur.fetchall() 
          

def execute(file_path: str, variables: dict) -> None:
    with open(file_path) as file:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute(file.read(), variables)
        # INSERT, UPDATE, DELETE... need to be committed
        con.commit()
