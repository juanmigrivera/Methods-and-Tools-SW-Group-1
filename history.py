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
