import sqlite3
import inventory

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

    def checkOut(self):
        inventory = Inventory(self.database_name) 

        def checkOut(self):
        # Instantiate Inventory with the same database
        inventory = Inventory(self.database_name)

        try:
            # Begin transaction
            self.connection.execute("BEGIN")
            select_query = "SELECT ISBN, quantity FROM cart WHERE userID = ?"
            self.cursor.execute(select_query, (self.userID,))
            items = self.cursor.fetchall()
            
            all_updated = True
            if items:
                for ISBN, quantity in items:
                    # Use the decrease_stock method from the Inventory class to update stock
                    if not inventory.decrease_stock(ISBN, quantity):
                        all_updated = False
                        break

                if all_updated:
                    # Clear cart after successful inventory update and checkout
                    clear_cart = "DELETE FROM cart WHERE userID = ?"
                    self.cursor.execute(clear_cart, (self.userID,))
                    self.connection.commit()
                    print("Checkout successful. Cart is now empty.")
                else:
                    print("Checkout failed due to inventory issues.")
                    self.connection.rollback()
            else:
                print("No items in cart to checkout.")
                self.connection.rollback()
        except sqlite3.Error as e:
            print(f"An error occurred during checkout: {e}")
            self.connection.rollback()
        finally:
            inventory.close_connection()

    def close_connection(self):
        self.connection.close()

    
