
from BudgetTracker import BudgetTracker

class MainMenu:
    def __init__(self):
        self.greetings=[]

    def greet_user(self):
        print("welcome to your BudgetTracker!\n")
        name = input("please enter your name: ")
        print("Hello" + " " + name + " " + "let's get started with your budget tracking!")
        return name

    # I added in a menu section that would allow users to have options to choose from

    def menu(self):
        print("choose one of the options below")
        print("1. add income")
        print("2. add expenses")
        print("3. list transactions")
        print("4. filter transactions")
        print("5. summarize transactions")
        print("6. Set Transaction Threshold")
        print("0. exit")

Bt=BudgetTracker()
main_menu=MainMenu()

main_menu.greet_user()

while True:
    main_menu.menu()
    choice=int(input("enter your choice: "))
    try:
        if choice==1:
            Bt.add_income()
        elif choice==2:
            Bt.add_expense()
        elif choice==3:
            Bt.list_transactions()
        elif choice==4:
            Bt.filter_transactions()
        elif choice==5:
            Bt.summarize_Transactions()
        elif choice==6:
            Bt.set_threshold()
        elif choice==0:
            print("Exiting program. Thank you for your time!")
            break
        else:
            print("please enter a valid choice\n")
    except ValueError:
        print("please enter a valid choice\n")


