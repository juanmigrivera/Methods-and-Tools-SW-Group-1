import sqlite3

class Inventory:

    def __init__(self, database_Name="methods.db"):
        self.database_Name = database_Name
        self.connection = sqlite3.connect(database_Name)
        self.cursor =self.connection.cursor()

    def viewInventory(self):
        self.cursor.execute("SELECT * FROM Inventory")
        inventory = self.cursor.fetchall()
        if inventory:
            print("Inventory:")
            separator = "-" * 120
            print(separator)
            print(f"{'ISBN':<20}{'Title':<25}{'Author':<25}{'Genre':<25}{'Pages':<10}{'Release Date':<15}{'Price':<10}{'Stock':<10}")
            print(separator)
            for item in inventory:
                print(f"{item[0]:<20}{item[1]:<25}{item[2]:<25}{item[3]:<25}{item[4]:<10}{item[5]:<15}{item[6]:<10}{item[7]:<10}")
                print(separator)
        else:
            print("Inventory is empty.")
        
    def searchInventory(self):
        title = input ("Enter the title you want to search for: ")
        self.cursor.execute("SELECT * FROM Inventory WHERE title=?", (title,))
        results=self.cursor.fetchall()
        if results:
            print("Search Results: ")
            for items in results:
                print(item)
            else
                print("No results found for '{}'.".format(title))

    
