import sqlite3

# Connecting to sqlite
# connection object
conn = sqlite3.connect('instance/database.db')
# cursor object
cursor_obj = conn.cursor()

def create_table():
    # Creating table
    table = """
        CREATE TABLE IF NOT EXISTS (
            ID INTEGER PRIMARY KEY NOT NULL, 
            FNAME VARCHAR(20), 
            LNAME VARCHAR(20),
            CITY VARCHAR(20), 
            CCODE CHAR(2));
            """

    cursor_obj.execute(table)
    
    print("Table is Ready")
    # Close the connection
    conn.close()