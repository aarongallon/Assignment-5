import sqlite3

conn = sqlite3.connect('baking_info')
curr = conn.cursor()


#Create the Baking_Info table
curr.execute('''
    CREATE TABLE IF NOT EXISTS Baking_Info(
        entry_id PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        Name TEXT NOT NULL,
        Phone_Number TEXT NOT NULL,
        Security_Level INTEGER NOT NULL,
        Login_Password TEXT NOT NULL
    )
    ''')