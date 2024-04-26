import sqlite3

class Cart:
    # contructor for cart class
    def __init__(self, userID, database_Name="methods.db"):
        self.userID = userID
        self.database_Name = database_Name
        self.connection = sqlite3.connect(database_Name)
        self.cursor = self.connection.cursor()

    def viewCart(self):
        try:
            query = 
            """
            SELECT inventory.title, inventory.price, cart.quantity
            FROM cart
            JOIN inventory ON cart.ISBN = inventory.ISBN
            WHERE cart.userID = ?
            """
            self.cursor.execute(query, (self.userID,))
            items = self.cursor.fetchall()
            if items:
                print("Your Cart:")
                for item in items:
                    print(f"Title: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")
            else:
                print("Your cart is empty.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            
   def addtoCart(self, ISBN, quantity):
       try:
            # Check if the item is available in the inventory
            check_inventory = "SELECT quantity FROM inventory WHERE ISBN = ?"
            self.cursor.execute(check_inventory, (ISBN,))
            inventory_quantity = self.cursor.fetchone()
