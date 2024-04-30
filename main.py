from user import *
from cart import *
from inventory import *
from history import *



def inventoryMenu(inventory):
    while True:
        print("Cart Information Menu:")
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
        
def cartMenu(cart, userID):
    while True:
        print("Inventory Information Menu:")
        print("0. Go Back")
        print("1. View Cart")
        print("2. Add items to cart")
        print("3. Remove an item from cart")
        print("4. Checkout")
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            break
        elif option == "1":
            cart.viewCart(userID)
        elif option == "2":
            cart.addToCart()
        elif option == "3":
            cart.removeFromCart()
        elif option == "4":
            cart.checkOut()
        else:
            print("That's not a menu option. Please try again.")

        print()


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart(userID=12-3456)
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
def mainMenu(user, cart, inventory, history, userID):
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
            user.displayAccountInfo()

        elif(option == "2"):
            inventoryMenu(inventory)

        elif(option == "3"):
            cartMenu(cart, userID)

        elif(option == "4"):
            history.displayOrderHistory(user)
            
        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()


def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
