#set up default values in the warehouse system: Inventory and account
#input account initial balance 10,000.
import warehousefunctions
file_name1= input("Please enter a name for inventory (i.e. .txt): ")
file_name2= input("Please enter a name for balance (i.e. .txt): ")
file_name3= input("Please enter a name for history (i.e. .txt): ")

inventory = warehousefunctions.loading_inventory(file_name1)
balance = warehousefunctions.loading_balance(file_name2)
history = warehousefunctions.loading_history(file_name3)

option = ""

account = 10000
#put product name, amount and unit price onto dictionary- Shampoo
inventory_dict = {
    "shiseido": {"unit_price": 20, "amount": 18 },
    "l'Oréal": {"unit_price":15, "amount": 22 },
    "klorane": {"unit_price": 12, "amount": 30 },
}
history = []


#Insert while loop to run commands
while True:
    print("Hiya user, welcome to warehouse system! See the available commands:\n ")
    print("exit -to log out\n")
    print("sale -record the sales of your products")
    print("purchase -record the purchase of your products")
    print("inventory -to display inventory")
    print("balance -the money in and out of your account")
    print("account- balance on the current account")
    print("history - the update record in the system\n")
    command = input("Provide a command: ").lower()

#Enter'sale': command entered for selected product name -  unit price, quantity
#display sales record and updated- sale quantity should not exceed the inventory
#****my question!shall I only restrict my items listed in the dictionary in sale? How to do that?
    if command == "sale":
        key = input("Provide the name of product sold: ").lower()
        if key not in inventory_dict.keys():
            print("This product does not exist.")
            continue
        unit_price = float(input("Provide the unit price: "))
        quantity = int(input("Provide the quantity sold: "))
        sales = unit_price * quantity
        inventory_dict[key]["amount"] -= quantity
        account = account + sales
        print(f"This deal- {key} brought you {sales} euros revenue.")
        change = (f"This deal -{key} brought you {sales} euros revenue.")
        history.append(change) 

    elif command == "purchase":
      key = input("Provide the name of product bought: ").lower()
      unit_price = float(input("Provide the unit price: "))
      quantity = int(input("Provide the quantity purchased: "))
      purchase = unit_price * quantity
      print(f"This deal - {key} cost you {purchase} euros.")
      change = (f"This deal-{key} cost you {purchase} euros.")
      history.append(change)

      if purchase > account:
          print("Current balance is not enough to purchase these products.")
          continue
      inventory_dict[key] = {}
      inventory_dict[key]['unit_price'] = unit_price
      inventory_dict[key]['amount'] = quantity
      print(key)
      print(inventory_dict[key]['unit_price'])
      print(inventory_dict[key]['amount'])
      account = account - purchase
      
      

#how to display inventory in the dictionary? balance >0 if balance =< account true, acc -= purchase

        
    elif command == "account":
        print(account)
    
    elif command == "balance":
        balance_command = input("Enter 'add' to add money or 'subtract' to subtract money: ")
        if balance_command == "add":
            amount = float(input("Enter an amount to add: "))
            account = account + amount
            print(f"You have added {amount} euros onto the account")
            change = (f"You have added {amount} euros onto the account")
            history.append(change)
        elif balance_command == "subtract":
            amount = float(input("Enter an amount to subtract: "))
            if amount > account:
                print("It's invalid input! Money you wish to subtract cannot exceed current balance.")
            else:
                account = account - amount
                print(f"You have withdrawn {amount} euros from the account")
                change = (f"You have withdrawn {amount} euros from the account")
                history.append(change)
        else:
            print("It's invalid input! Please try again. ")

    elif command == "history":
        from_value = input("Please enter the from value: ")
        to_value = input("Please enter the to value: ")
        if from_value == "" and to_value == "":
            for i in history:
                print(i)
        elif from_value != "" and to_value == "":
            for i in history[int(from_value)-1:]:
                print(i)
        elif from_value == "" and to_value !="":
            for i in history[:int(to_value)+1]:
                print(i)
        else:
            for i in history[int(from_value)-1:int(to_value)]:
                print(i)
    
    elif command == "inventory":
        print("Inventory status:\n")
        print(inventory_dict)


    elif command == "warehouse":
        key = input("Enter the name of the product: ")
        print(key)
        print(inventory_dict[key]['unit_price'])
        print(inventory_dict[key]['amount'])

    elif command == "exit":
        print("You will exit the system.")
        warehousefunctions.saving_inventory(file_name1, inventory)
        warehousefunctions.saving_balance(file_name2, balance)
        warehousefunctions.saving_history(file_name3, history)
        break


    else:
        print("It's invalid input! Please try again or enter exit to leave. ")

