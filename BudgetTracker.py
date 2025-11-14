# I started with this greet_user function so that it will be creating a personalized experience for the user(s)
# I included the  datetime library because I think the project will involve some kind of time manipulation

from datetime import datetime, timedelta
Transactions=[]

def greet_user():
    print("welcome to your BudgetTracker\n")
    name=input("please enter your name: ")
    print("Hello"+" "+name+" "+"let's get started with your budget tracking!\n")
    return name

#I added in a menu section that would allow users to have options to choose from

def menu():
    print("choose one of the options below")
    print("1. add transactions")
    print("2. list transactions")
    print("3. summarize budget")
    print("4. view transaction history")
    print("5. exit")


#I defined the add_transactions function so that it can give the user options to add in their transaction details
#It then stores the transaction made in the dictionary created inside the add_transaction function and appends it to the Transactions list

def add_transactions():
    date=input("enter date of transaction (dd/mm/yyyy): \n")
    amount=input("enter amount of transaction: ")
    transaction_type=input("enter type of transaction: ")
    description=input("enter description of transaction: ")
    transaction = {
        "date": date,
        "amount": amount,
        "description": description,
        "transaction_type": transaction_type
    }
    Transactions.append(transaction)
    print("transaction added successfully\n")

#I created a list_transaction function as well that run when the user wants to see a list of all his transactions. added in the /n to create space for visibility and the enumarate function to count the transactions made

def list_transactions():
    if not Transactions:
        print("No transactions recorded yet.\n")
        return
    for y, x in enumerate(Transactions, start=1):
        print(f"transaction 1: {x['date']} | {x['amount']} | {x['description']}\n")

greet_user()

while True:
    menu()
    choice=int(input("enter your choice: \n"))
    if choice==1:
        add_transactions()
    elif choice==2:
        list_transactions()
    else:
        print("You entered a wrong choice")







