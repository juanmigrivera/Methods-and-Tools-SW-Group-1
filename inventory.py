import sqlite3

class Inventory:
    def __init__(self, database_name="methods.db"):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def view_inventory(self):
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





    def search_inventory(self):
        title= input("Enter the title you want to search for: ")
        self.cursor.execute("SELECT * FROM inventory WHERE title=?", (title,))
        results = self.cursor.fetchall()
        if results:
            print("Search Results:")
            separator = "-" * 120
            print(separator)
            print(f"{'ISBN':<20}{'Title':<25}{'Author':<25}{'Genre':<25}{'Pages':<10}{'Release Date':<15}{'Price':<10}{'Stock':<10}")
            print(separator)
            for item in results:
                print(f"{item[0]:<20}{item[1]:<25}{item[2]:<25}{item[3]:<25}{item[4]:<10}{item[5]:<15}{item[6]:<10}{item[7]:<10}")
                print(separator)
        else:
            print("No results found for '{}'.".format(title))

    def decrease_stock(self, ISBN, quantity=1):
        try:
            self.cursor.execute("SELECT * FROM inventory WHERE ISBN=?", (ISBN,))
            item = self.cursor.fetchone()
            if item:
                current_stock = item[7]  
                if current_stock >= quantity:
                    new_stock = current_stock - quantity
                    self.cursor.execute("UPDATE Inventory SET stock=? WHERE ISBN=?", (new_stock, ISBN))
                    self.connection.commit()
                    print("Stock for ISBN {} decreased by {} units.".format(ISBN, quantity))
                    return True
                else:
                    print("Insufficient stock for ISBN {}.".format(ISBN))
                    return False
            else:
                print("ISBN {} not found in inventory.".format(ISBN))
                return False
        except sqlite3.Error as e:
            print(f"An error occurred while decreasing stock: {e}")

    

    # Getters and setters
    def get_database_name(self):
        return self.database_name

    def set_database_name(self, new_database_name):
        self.database_name = new_database_name

    

    
