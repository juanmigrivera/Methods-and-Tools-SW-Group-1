import sqlite3
from datetime import datetime
from inventory import Inventory
from history import OrderHistory

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
            self.cursor.execute(query,(userID,))
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
            check_inventory = "SELECT stock FROM inventory WHERE ISBN = ?"
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
        

        
        try:
            inventory=Inventory()
            history=OrderHistory()

            select_query = "SELECT ISBN, quantity FROM cart WHERE userID = ?"
            self.cursor.execute(select_query, (userID,))
            items = self.cursor.fetchall()
            
            if not items:
                print("Your cart is empty. There is nothing to checkout.")
                return 
           
            
            total_cost = 0
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            for item in items:
                ISBN, quantity=item
                book_query = "SELECT price FROM inventory WHERE ISBN = ?"
                self.cursor.execute(book_query, (ISBN,))
                price=self.cursor.fetchone()[0]
                total_cost+= price * quantity
                inventory.decrease_stock(ISBN, quantity)
                
            order_number=history.createOrder(userID, len(items), total_cost, current_date)
            
            history.addOrderItems(userID, order_number)
            
            delete_query = "DELETE FROM cart WHERE userID= ?"
            self.cursor.execute(delete_query, (userID,))
            self.connection.commit()
            
            print("Checkout successful.")
            
        except sqlite3.Error as e:
            print(f"An error occured during checkout: {e}")
        
            
    def close_connection(self):
        self.connection.close()
