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
            
   def addToCart(self, ISBN, quantity=1):
        try:
            # Checks if the item is available in the inventory
            check_inventory = "SELECT quantity FROM inventory WHERE ISBN = ?"
            self.cursor.execute(check_inventory, (ISBN,))
            inventory_quantity = self.cursor.fetchone()
            
            if inventory_quantity and inventory_quantity[0] >= quantity:
                # Checks if item already in cart
                check_cart = "SELECT quantity FROM cart WHERE userID = ? AND ISBN = ?"
                self.cursor.execute(check_cart, (self.userID, ISBN))
                cart_item = self.cursor.fetchone()
                
                if cart_item:
                    # Updates quantity if already in cart
                    new_quantity = cart_item[0] + quantity
                    update_cart = "UPDATE cart SET quantity = ? WHERE userID = ? AND ISBN = ?"
                    self.cursor.execute(update_cart, (new_quantity, self.userID, ISBN))
                else:
                    # Adds new item to cart
                    insert_cart = "INSERT INTO cart (userID, ISBN, quantity) VALUES (?, ?, ?)"
                    self.cursor.execute(insert_cart, (self.userID, ISBN, quantity))
                
                self.connection.commit()
                print("Item added to cart successfully.")
            else:
                print("Requested quantity not available in inventory.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            
    def removeFromCart(self, ISBN):
        try:
            delete_query = "DELETE FROM cart WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(delete_query, (self.userID, ISBN))
            self.connection.commit()
            print("Item removed from cart.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
