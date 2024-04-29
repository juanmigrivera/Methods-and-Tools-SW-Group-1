import sqlite3
import random

class OrderHistory:
    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()
    def viewHistory(self, userID):
        try:
            query = """
            SELECT OrderNumber, ItemNumber, Cost, Date
            FROM Orders
            WHERE UserID = ?
            """
            self.cursor.execute(query, (userID,))
            orders = self.cursor.fetchall()
            if orders:
                print("Order History:")
                for order in orders:
                    print(f"Order Number: {order[0]}, Number of Items: {order[1]}, Cost: {order[2]}, Date: {order[3]}")
            else
                print("No order history")
    def viewOrder(self, userID, orderID):
        try:
            query = "SELECT * FROM Orders WHERE UserID = ? AND OrderNumber = ?"
            self.cursor.execute(query, (userID, orderID))
            order = self.cursor.fetchone()
            if order:
                query = """
                SELECT Inventory.Title, Inventory.Author, Inventory.Price, OrderItems.Quantity
                FROM OrderItems
                JOIN Inventory ON OrderItems.ISBN = Inventory.ISBN
                WHERE OrderItems.OrderNumber = ?
                """
                self.cursor.execute(query, (orderID,))
                order_items = self.cursor.fetchall()
                if order_items:
                    print(f"Order items for Order ID {orderID}:")
                    for item in order_items:
                        print(f"Title: {item[0]}, Author: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
                else:
                    print(f"No items for order ID")
            else:
                print(f"Order ID does not belong to user")
    def createOrder(self, userID, quantity, cost, date):
        
                
            
