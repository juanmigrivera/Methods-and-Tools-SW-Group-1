import sqlite3

from inventory import Inventory

class Cart:
    def __init__(self, database_name="methods.db"):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def viewCart(self, userID):
        try:
            query = """
            SELECT inventory.title, inventory.price, cart.quantity 
            FROM cart 
            JOIN inventory ON cart.ISBN = inventory.ISBN 
            WHERE cart.userID = ?
            """
            self.cursor.execute(query, (userID,))
            items = self.cursor.fetchall()

            if items:
                print("Your Cart:")
                print('-' * 70)  
                print(f"{'Title':<30}{'Price':<15}{'Quantity':<15}")
                print('-' * 70)
                for item in items:
                    title, price, quantity = item
                    print(f"{title:<30}{price:<15}{quantity:<15}")
                print('-' * 70)
            else:
                print("Your cart is empty.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def addToCart(self, userID, ISBN, quantity=1):
        try:
            check_inventory = "SELECT quantity FROM inventory WHERE ISBN = ?"
            self.cursor.execute(check_inventory, (ISBN,))
            inventory_quantity = self.cursor.fetchone()
            
            if inventory_quantity and inventory_quantity[0] >= quantity:
                check_cart = "SELECT quantity FROM cart WHERE userID = ? AND ISBN = ?"
                self.cursor.execute(check_cart, (userID, ISBN))
                cart_item = self.cursor.fetchone()
                
                if cart_item:
                    new_quantity = cart_item[0] + quantity
                    update_cart = "UPDATE cart SET quantity = ? WHERE userID = ? AND ISBN = ?"
                    self.cursor.execute(update_cart, (new_quantity, userID, ISBN))
                else:
                    insert_cart = "INSERT INTO cart (userID, ISBN, quantity) VALUES (?, ?, ?)"
                    self.cursor.execute(insert_cart, (userID, ISBN, quantity))
                
                self.connection.commit()
                print("Item added to cart successfully.")
            else:
                print("Requested quantity not available in inventory.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def removeFromCart(self, userID, ISBN):
        try:
            delete_query = "DELETE FROM cart WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(delete_query, (userID, ISBN))
            self.connection.commit()
            print("Item removed from cart.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            
    def checkOut(self, userID):
        inventory = Inventory(self.database_name)

        try:
            self.connection.execute("BEGIN")
            select_query = "SELECT ISBN, quantity FROM cart WHERE userID = ?"
            self.cursor.execute(select_query, (userID,))
            items = self.cursor.fetchall()
            
            all_updated = True
            if items:
                for ISBN, quantity in items:
                    if not inventory.decrease_stock(ISBN, quantity):
                        all_updated = False
                        break

                if all_updated:
                    clear_cart = "DELETE FROM cart WHERE userID = ?"
                    self.cursor.execute(clear_cart, (userID,))
                    self.connection.commit()
                    print("Checkout successful. Cart is now empty.")
                else:
                    self.connection.rollback()
                    print("Checkout failed due to inventory issues.")
            else:
                self.connection.rollback()
                print("No items in cart to checkout.")
        except sqlite3.Error as e:
            self.connection.rollback()
            print(f"An error occurred during checkout: {e}")
        finally:
            inventory.close_connection()
