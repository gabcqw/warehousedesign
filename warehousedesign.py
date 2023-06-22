#set up default values in the warehouse system: Inventory and account
#input account initial balance 10,000.
account = 10000
#put product name, amount and unit price onto dictionary- Shampoo
inventory_dict = {
    "Shiseido": {"unit_price", 20, "amount", 18 },
    "L'Oréal": {"unit_price", 15, "amount", 22 },
    "Klorane": {"unit_price", 12, "amount", 30 },
}

print("Hiya user, welcome to warehouse system! See the available commands:\n ")
print("exit -to log out")
print("sale -record the sales of your products")
print("purchase -record the purchase of your products")
print("balance -the money in and out of your account")
print("account- balance on the current account")
print("history - the update record in the system")



#Insert while loop to run commands
while True:
    command = input("Provide a command: ")

#Enter'sale': command entered for selected product name -  unit price, quantity
#display sales record and updated- sale quantity should not exceed the inventory
#****my question!shall I only restrict my items listed in the dictionary in sale? How to do that?
    if command == "sale":
        key = input("Provide the name of product sold: ")
        unit_price = float(input("Provide the unit price: "))
        quantity = int(input("Provide the quantity sold: "))
        sales = unit_price * quantity
        balance = account + sales
#*****how to display inventory in the dictionary?*****
        print(f"This deal brought you {sales} euros revenue.")

    elif command == "exit":
        print("You will exit the system.")
        break

    elif command == "purchase":
      key = input("Provide the name of product bought: ")
      quantity = float(input("Provide the quantity purchased: "))
      purchase = unit_price * quantity
      balance = account - purchase
#*****how to display inventory in the dictionary?*****

        
    elif command == "account":
        pass


    elif command == "warehouse":
        name = input("Enter the name of the product: ")
        pass

    elif command == "account":
        name = input("Check your current account balance. ")
        pass
    else:
        print("It's invalid input! Please try again. ")