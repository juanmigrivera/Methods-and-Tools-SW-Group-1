from user import *
from cart import *
from inventory import *
from history import *


    

def inventoryMenu(inventory):
    while True:
        print("Inventory Information Menu:")
        print("0. Go Back")
        print("1. View Inventory")
        print("2. Search Inventory")
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            break
        elif option == "1":
            inventory.view_inventory()
        elif option == "2":
            inventory.search_inventory()
        else:
            print("That's not a menu option. Please try again.")

        print()
        
def cartMenu(cart, user):
    while True:
        print("Cart Information Menu:")
        print("0. Go Back")
        print("1. View Cart")
        print("2. Add items to cart")
        print("3. Remove from cart")
        print("4. Check out")
        
        
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            break
        elif option == "1":
            cart.viewCart(user)
        elif option == "2":
           ISBN= input("Enter the ISBN of the book you want to add: ")
           cart.addToCart(user, ISBN)
        elif option == "3":
           ISBN= input("Enter the ISBN of the book you want to remove: ")
           cart.removeFromCart(user, ISBN)
        elif option == "4":
            cart.checkOut()
        else:
            print("That's not a menu option. Please try again.")

        print()

def UserMenu(user):
        user.viewAccountInformation()
        
def HistoryMenu(history, user):
    while True:
        print("History Information Menu:")
        print("0. Go Back")
        print("1. View Order History")
        print("2. View Order")
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            break
        elif option == "1":
            history.viewHistory(user)
        elif option == "2":
            OrderNumber=input("Enter Order Number: ")
            history.viewOrder(user, OrderNumber)
        else:
            print("That's not a menu option. Please try again.")

        print()

## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory()
    history = OrderHistory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        print("4. Order Information")
        option = input("Enter your menu choice: ")
        print()

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")
            break
        elif(option == "1"):
            UserMenu(user)

        elif(option == "2"):
            inventoryMenu(inventory)

        elif(option == "3"):
            cartMenu(cart, user.userID)

        elif(option == "4"):
            HistoryMenu(history, user.userID)
            
        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()


def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
