from BudgetTracker import BudgetTracker
# Import the BudgetTracker class so the main file can call its methods


class MainMenu:

    def greet_user(self):
        # Greets the user at the start of the program
        print("welcome to your BudgetTracker!\n")
        name = input("please enter your name: ")
        print("Hello" + " " + name + " " + "let's get started with your budget tracking!")
        return name  # Return user's name in case it's needed later

    def menu(self):
        # Displays the main options the user can choose from
        print("choose one of the options below")
        print("1. add income")
        print("2. add expenses")
        print("3. list transactions")
        print("4. filter transactions")
        print("5. summarize transactions")
        print("6. Set Transaction Threshold")
        print("0. exit")


Bt = BudgetTracker()  # Create a BudgetTracker object to manage all transactions and logic
main_menu = MainMenu()  # Create the menu object for user interaction

main_menu.greet_user()  # Show the greeting message once at program start

# Program loop — runs until the user selects exit (choice 0)
while True:
    main_menu.menu()  # Show menu options

    try:
        User_input = input("enter your choice: ")
        if User_input == " ":
            print('choice cannot be blank. please enter a valid choice')
            continue
        choice = int(User_input)
        # Match user input to menu actions
        if choice == 1:
            Bt.add_income()            # Calls method to add an income transaction
        elif choice == 2:
            Bt.add_expense()           # Calls method to add an expense transaction
        elif choice == 3:
            Bt.list_transactions()     # Displays all recorded transactions
        elif choice == 4:
            Bt.filter_transactions()   # Allows filtering by type, month, description
        elif choice == 5:
            Bt.summarize_Transactions()  # Shows total summary + per-category summary
        elif choice == 6:
            Bt.set_threshold()         # Allows user to set a budget limit for a category
        elif choice == 0:
            print("Exiting program. Thank you for your time!")
            break                      # Stops the loop → exits the program
        else:
            # Handles numbers that are not recognized menu options
            print("please enter a valid choice\n")

    except ValueError:
        # Handles cases where user types something that cannot be converted to int
        print("please enter a valid choice\n")
