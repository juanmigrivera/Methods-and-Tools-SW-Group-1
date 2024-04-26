import sqlite3

class Cart:
    # contructor for cart class
    def __init__(self, database_Name="methods.db"):
        self.database_Name = database_Name
        self.connection = sqlite3.connect(database_Name)
        self.cursor = self.connection.cursor()
   
