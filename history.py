import sqlite3
import random

class OrderHistory:
    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()
        
    def viewHistory(self, userID):
        try:
            
            self.cursor.execute(("SELECT * FROM Orders WHERE UserID = ? " ),(userID,))
            
            orders = self.cursor.fetchall()
            if len(orders) > 0:
                
                print("Order History:")
                for order in orders:
                    print(f"Order Number: {order[0]}, UserID: {order[1]}, Item Number: {order[2]}, Cost: {order[3]}, Date:  {order[4]}")
            else:
                print("No order history")
        except:
            print("Error")
            
    def viewOrder(self, UserID, OrderNumber):
        
        try:
            query = "SELECT * FROM Orders WHERE UserID = ? AND OrderNumber = ?"
            self.cursor.execute(query, (UserID, OrderNumber))
            order = self.cursor.fetchone()
            if order:
                query = """
                SELECT Inventory.Title, Inventory.Author, Inventory.Price, OrderItems.Quantity
                FROM OrderItems
                JOIN Inventory ON OrderItems.ISBN = Inventory.ISBN
                WHERE OrderItems.OrderNumber = ?
                """
                self.cursor.execute(query, (OrderNumber,))
                order_items = self.cursor.fetchall()
                if order_items:
                    print(f"Order items for Order ID {OrderNumber}:")
                    for item in order_items:
                        print(f"Title: {item[0]}, Author: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
                else:
                    print(f"No items for order ID")
            else:
                print(f"Order ID does not belong to user")
        except:
            print("Error")
                
    def createOrder(self, userID, quantity, cost, date):
        try:
            while True:
                order_number = str(random.randint(100000, 999999))
                query = "SELECT * FROM Orders WHERE OrderNumber = ?"
                self.cursor.execute(query, (order_number,))
                if not self.cursor.fetchone():
                    break
            insert_query = "INSERT INTO Orders (OrderNumber, UserID, ItemNumber, Cost, Date) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(insert_query, (order_number, userID, quantity, cost, date))
            self.connection.commit()
            return order_number
        except:
            print("Error")

    def addOrderItems(self, userID, orderID):
        try:
            copy_query = """
            INSERT INTO OrderItems (OrderNumber, ISBN, Quantity)
            SELECT ?, ISBN, Quantity FROM Cart WHERE UserID = ?
            """
            self.cursor.execute(copy_query, (orderID, userID))
            self.connection.commit()
            print("Order items added successfully")
        except:
            print("Error")

    def close_connection(self):
        self.connection.close()
    
                
