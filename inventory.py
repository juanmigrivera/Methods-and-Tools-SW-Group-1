import sqlite3
import inventory

class Inventory:

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
                else:
                    print("No results found for '{}'.".format(title))

        def decrease_stock(self, ISBN=None, quantity=None):
            if ISBN is None:
                ISBN = input("Enter the ISBN of the item you want to decrease the stock for: ")
            if quantity is None:
                quantity = int(input("Enter the quantity to decrease: "))

            try:
                self.cursor.execute("SELECT stock FROM Inventory WHERE ISBN=?", (ISBN,))
                item = self.cursor.fetchone()
                if item:
                    current_stock = item[0]
                    if current_stock >= quantity:
                        new_stock = current_stock - quantity
                        self.cursor.execute("UPDATE Inventory SET stock=? WHERE ISBN=?", (new_stock, ISBN))
                        self.connection.commit()
                        print(f"Stock for ISBN {ISBN} decreased by {quantity} units.")
                        return True
                    else:
                        print(f"Insufficient stock for ISBN {ISBN}.")
                        return False
                else:
                    print(f"ISBN {ISBN} not found in inventory.")
                    return False
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return False

        def get_database_name(self):
            return self.database_name

        def set_database_name(self, new_database_name):
            self.database_name = new_database_name

        def close_connection(self):
            self.connection.close()

    

    
