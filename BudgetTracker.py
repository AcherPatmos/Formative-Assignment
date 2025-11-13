# I started with this greet_user function so that it will be creating a personalized experience for the user(s)
def greet_user():
    print("welcome to your BudgetTracker")
    name=input("please enter your name: ")
    print("Hello"+" "+name+" "+"let's get started with your budget tracking!")
    return name
greet_user()
#I added in a menu section that would allow users to have options to choose from
def menu():
    print("choose one of the options below")
    print("1. add transactions")
    print("2. list transactions")
    print("3. summarize budget")
    print("4. view transaction history")
    print("5. exit")
menu()

def add_transactions():
    date=input("enter date of transaction: ")
    amount=input("enter amount of transaction: ")
    description=input("enter description of transaction: ")
    print(f"Your transaction details are {date},{amount},{description}")
choice=int(input("please enter your choice: "))
if choice==1:
    add_transactions()

else:
    print("You entered a wrong choice")
#
# from datetime import datetime, timedelta
#
# def add_transaction():
#     enter_date=input("enter date of the transaction (dd/yy/mm): ")
#     amount=int(input("enter amount you transacted: "))
#     description=input("enter description of the transaction: ")

#
# transaction = {
#         "date": date_obj,
#         "amount": amount,
#         "category": category,
#         "description": description,
#         "type": t_type
#     }
#     transactions.append(transaction)
#     print("Transaction added successfully!")
