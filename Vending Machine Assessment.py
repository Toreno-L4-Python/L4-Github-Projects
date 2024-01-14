import random ##Added this in for my fun little kick function in Line 46
import sys ##This is so i can terminate the program for when the user chooses to exit with "sys.exit()"
from datetime import datetime ##Makes it so when making a receipt, it will print out the current date 
CurrentDate = datetime.now()
FormattedDate = CurrentDate.strftime("%B %d, %Y") ##to format the current date for the receipt Ex. January 12, 2024
import time ##Added this in so i can create a delay effect to simulate a receipt printer and also to keep it from printing sentences too instant or fast. Also cause it looks nice and easy to read when each print comes out one at a time.
spacing = 1
itemlist = [ ##a list filled with dictionaries for each product and their respective values.
        ##Snacks
        {"name" : "Lay's Chips", "price" : 7.00, "amount" : 1, "slot" : "1"}, 
        {"name" : "Doritos", "price" : 8.45, "amount" : 2, "slot" : "2"},
        {"name" : "Cheez-It", "price" : 6.50, "amount" : 3, "slot" : "3"},
        ##Hot Beverages
        {"name" : "Arwa Hot Chocolate", "price" : 4.20, "amount" : 4, "slot" : "4"},
        {"name" : "Starbucks Doubleshot Espresso", "price" : 2.50, "amount" : 5, "slot" : "5"},
        {"name" : "Nescafe R-T-D Coffee", "price" : 3.65, "amount" : 6, "slot" : "6"},
        ##Cold Beverages
        {"name" : "Coke", "price" : 1.50, "amount" : 7, "slot" : "7"},
        {"name" : "Pepsi", "price" : 1.60, "amount" : 8, "slot" : "8"},
        {"name" : "7-Up", "price" : 1.50, "amount" : 9, "slot" : "9"}
    ]
def startup(): ##turned about 99% of the code into a function to make it easier to return back to the menu after a purchase
    spacing = 1
    print("\n[Welcome To Our Vending Machine]\n")
    for item in itemlist:
        print(f"[{item['slot']}]{item['name']: <30} => {item['price']:.2f} AED") #This is to keep the list of items and their prices from looking to jumbled and disorganized

        if spacing % 3 == 0:
            print()  # This is to add in a space after every 3 slots to seperate each category of items

        spacing += 1


    choice = input("Please select the item's ID number (Ex. [ID number] Lay's Chips) to purchase or type 'Exit' to leave: ") ##So the User can choose to either Exit for select an item
    
    ##UserBalance = int(input("\nPlease insert cash: "))

    for item in itemlist:
        
        if choice == "Exit" or choice == "exit": ##to check if the User chooses to exit the vending machine menu.
            print("Thank you for using our vending machine!")
            time.sleep(0.5)
            print("Goodbye.")
            sys.exit()

        elif choice == "Kick" or choice == "kick": ##It isnt a TRUE vending machine if you cant kick it. I did not include "kick" in the given choices as I'd like the user to find it themselves as a little secret.  
            if random.choice([True, False]): ## gives the user a chance to either get a random item or just shut down the machine.
                print("\nPhysical impact detected!")
                time.sleep(0.5)
                print("This machine will shut down to prevent any theft.")
                time.sleep(0.5)
                print("Goodbye.")
                time.sleep(0.5)
                sys.exit()
            else:
                randomitem = random.choice(itemlist) 
                print("--ERROR--")
                time.sleep(1)
                print(f"\nDispensing [{randomitem['name']}]...")
                randomitem['amount'] -= 1
                print(f"{randomitem['amount']}")
                item['amount'] = randomitem['amount']
                time.sleep(1)
                startup()
        if (choice) == item['slot']:
            print(f"\nYour selected item is [{item['name']}]\n")
            confirm = input("Confirm selection? Y/N: ") ##Confirmation bit so the User can back out if they change their mind or chose the wrong item ID
            if confirm in ["Y", "y"]:
                UserBalance = int(input("\nPlease insert cash: "))
                if item['amount'] > 0 and UserBalance >= item['price']: ##Checks if the chosen item is still in stock and if the User has enough balance
                    print(f"\nYou have purchased [{item['name']}] for [{item['price']:.2f} AED].\n")
                    Change = UserBalance - item['price'] ##calculates the User's change.
                    time.sleep(1)
                    print(f"Dispensing [{item['name']}]...\n")
                    time.sleep(1)
                    print("Processing your change...\n")
                    time.sleep(2)
                    print(f"Here is your exact change: {Change:.2f} AED.\n")
                    item['amount'] -= 1 ##This is so it takes away 1 amount of the item's stock.
                    receipt = input("Would you like a receipt Y/N?: ") ##Asks if the User wants a receipt or not.
                    
                    if receipt in ["Y", "y"]:
                        print("\nPlease wait as we print out your receipt...\n")
                        time.sleep(1)
                        print("******************* RECEIPT *******************")
                        time.sleep(0.5) ## 0.5s delay to simulate a printer in the terminal.
                        print(f"Date: {FormattedDate}")
                        time.sleep(0.5)
                        print("===============================================")
                        time.sleep(0.5)
                        print(f"{item['name']: <37} {item['price']:.2f}AED")
                        time.sleep(0.5)
                        print("===============================================")
                        time.sleep(0.5)
                        print(f"{'Total:': <37} {item['price']:.2f} AED")
                        time.sleep(0.5)
                        print(f"{'Payment:': <37} {UserBalance:.2f} AED")
                        time.sleep(0.5)
                        print(f"{'Change:': <37} {Change:.2f} AED")
                        time.sleep(0.5)
                        print("===============================================")
                        time.sleep(0.5)
                        print("Thank you for your purchase!")
                        time.sleep(0.5)
                        print("********************* END *********************\n")
                        time.sleep(2) ##2 second delay so it doesnt instantly write "Welcome to our vending machine" when returning back to the menu
                        startup()
                        
                    elif receipt in ["N", "n"]:
                        time.sleep(1)  
                        startup()
                    else:
                        print("Invalid Input...\n")
                        time.sleep(1)
                        print("No Receipt will be printed...")
                        time.sleep(1)
                        startup()

                elif UserBalance < item['price']: ## Goes in effect if the User does not have enough balance/money for their chosen item.
                    print("\nInsufficient balance...\n")
                    time.sleep(2)
                    startup()
                elif item['amount'] <=0: ## goes in effect if the selected item is out of stock.
                    print("\nThis item is out of stock...\n")
                    time.sleep(2)
                    startup()    
            elif confirm in ["N", "n"]:
                startup()
            else:
                print("\nInvalid Input...")
                time.sleep(1)
                startup()               
        elif choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"): ##this is to keep the User from inputting a value that is not a valid slot number, which are slot numbers 1 - 9.
            print("Invalid ID, Please try again...")
            time.sleep(1)      
            startup()
startup()

