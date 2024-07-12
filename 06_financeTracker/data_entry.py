from datetime import datetime

CATEGORIES = {'I': "Income", 'E': "Expense"}

def getDate(prompt, allowDefault=False):
    dateStr = input(prompt)

    if allowDefault and not dateStr:
        return datetime.today().strftime("%d-%m-%Y")
    
    try:
        validDate = datetime.strptime(dateStr, "%d-%m-%Y")
        return validDate.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format.\nEnter the date in DD-MM-YYYY format.")
        return getDate(prompt, allowDefault)

def getAmount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return getAmount()

def getCategory():
    category = input("Enter the category.\n'I' for Income.\n'E' for Expense.\n").upper()

    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category.\n'I' for Income.\n'E' for Expense.\n")
    return getCategory()

def getDescription():
    return input("Enter a description.\n")