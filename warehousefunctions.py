from ast import literal_eval
def loading_inventory(file_name):
    try:
        with open(file_name, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("This file does not exist. Please create new file. ")
        return {}
    
def saving_inventory(file_name, inventory):
    with open(file_name, 'w') as file:
        file.write(str(inventory))

def loading_balance(file_name): #account or balance? account value is intl/float
    try:
        with open(file_name, 'r') as file:
            return literal_eval(float(file.read()))
    except FileNotFoundError:
        print("This file does not exist. Please create new file. ")
        return {}
def saving_balance(file_name, balance):
    with open(file_name, 'w') as file:
        file.write(float(balance))

def loading_history(file_name):#history is a list ?how to use it? loke -.readline() ? 
    try:
        with open(file_name, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("This file does not exist. Please create new file. ")
        return []
def saving_history(file_name, history):
    with open(file_name, 'w') as file:
        file.write[(history)]