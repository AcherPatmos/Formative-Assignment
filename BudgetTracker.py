from datetime import datetime, timedelta
from tabulate import tabulate
from Transactions import Income, Expense # Imported the Income and Expense classes from Transaction

class BudgetTracker:
    def __init__(self):
        self.Transactions=[] # created an empty Transaction list to store all the transactions

        self.balance=0 # checks the money being recorded and adds on to the balance. it starts at 0

        self.thresholds = {} #a dictionary to keep categories that have expense limits as key value pairs with their amount limits

    def validate_date(self): # a helper function to help check if the user inputs the right date in the right format
        while True:
            date=input("Enter the date of the transaction (dd/mm/yyyy): \n")
            try:
                date = datetime.strptime(date, "%d/%m/%Y").date()
                if date.year < 2025:
                    print("Year cannot be below 2025! Please enter a valid year \n")
                    continue
                if date.year > 2025:
                    print("Year cannot be beyond 2025! Please enter a valid year \n")
                    continue
                return date
            except ValueError:
                print("Please enter a valid date and year \n")

    def get_amount(self): # a helper function to help validate the amount the user is writing
        # I used the while true loop to make sure the user would always be prompted to write a valid amount if they put in a negative number
        # Currencies are also not supported. The try is to handle invalid inputs gracefully instead of python crashing
        while True:
                try:
                    amount = float(input("Amount: $"))
                    if amount < 0:
                        print("Amount cannot be negative! please enter a valid amount")
                        continue
                    return amount
                except ValueError:
                    print("Please enter a valid number.")

    def add_income(self): # the add income function
        t_date = self.validate_date()
        amount= self.get_amount()
        description = input("enter transaction category(eg:Salary,Groceries): ").strip().lower()
        inc=Income(t_date,amount,description)
        self.Transactions.append(inc) # appends any valid recorded transaction to the transaction list
        self.balance+=amount # adds amount recorded to the self.balance attribute
        print(f"transaction recorded successfully Current balance= ${self.balance}")

    def add_expense(self): # the add expenses function
        t_date = self.validate_date()
        amount = self.get_amount()
        description = input("enter transaction category(eg:Salary,Groceries): ").strip().lower()
        exp=Expense(t_date,amount,description)
        self.Transactions.append(exp)
        self.balance-=amount
        self.check_threshold_warning(description) # uses the check threshold limit function to see if the user is not going over their set budget and issues warnings
        print(f"transaction recorded successfully Current balance= ${self.balance}")

    def list_transactions(self): #list transactions functionality
        if not self.Transactions:
            print("No transactions recorded yet.")
            return
        table=[] # created an empty table list to store the transactions already recorded
        for x in self.Transactions:
            table.append([x.date,x.t_type.upper(),x.amount,x.description]) # searches all the transactions recorded in self.Transactions and adds them to the table list
        headers=["Date","Type","Amount","Description"]
        print("Transactions list")
        print(tabulate(table,headers,tablefmt="fancy_grid"))
        print(f'current balance= ${self.balance}')

    def filter_transactions(self): #added in the filter Transactions function
        print("choose one of the filter options below: ")
        print("1. filter by Date")
        print("2. filter by Transaction type")
        print("3. filter by description")
        print("4. exit")
        while True: #created a loop to help the user make choices easily without having to restart the whole process
            option= int(input("Enter your choice: "))
            try:
                if option == 1:
                    self.filter_by_month()
                elif option == 2:
                    self.filter_by_type()
                elif option == 3:
                    self.filter_by_description()
                elif option == 4:
                    print("returning to main menu")
                    return
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("please enter a valid choice")

    def display_results(self, results): #this helper function helps display the filtered results
        if not results:
            print("No matching transactions found")
            return
        table = [
            [x.date.strftime("%Y/%m"), x.t_type.upper(), x.amount, x.description]
            for x in results
        ] #appends the results that matches what the user requested to this table list
        print("\nFiltered Results:")
        print(tabulate(table, ["Date", "Type", "Amount", "Description"], tablefmt="fancy_grid"))

    def filter_by_month(self): #this method filters by month
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        recorded_months = sorted({t.date.strftime("%Y-%m") for t in self.Transactions}) #sorts the recorded transaction months in chronological order
        print("\nRecorded months to filter:", ", ".join(recorded_months)) #shows the user which months are available to filter in case they forgot
        while True:
            dt = input("Enter a date (YYYY/MM): ")
            if len(dt) != 7 or dt[4] != "/":
                print("Invalid format! Use YYYY/MM (e.g., 2025/04).") #validates that the user is using the right date format
                continue
            results = [t for t in self.Transactions if t.date.strftime("%Y/%m") ==dt] #stores the data that matches the results the user wants
            if results:
                self.display_results(results) #if the results list is not empty, it will run the display result function which prints the results in a table
                return
            print("Invalid month or no transactions in that month.")

    def filter_by_type(self): #filters by type: expense or income
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        recorded_types = sorted({t.t_type for t in self.Transactions})
        print("\nAvailable transaction types:", ", ".join(t.lower() for t in recorded_types))
        while True:
            transaction_type = input("Enter a transaction type(income/expense): ")
            if transaction_type not in ["income", "expense"]:
                print("\nInvalid type! Must be 'income' or 'expense'.") # checks whether the user wrote the right transaction type
                continue
            if transaction_type not in recorded_types:
                print(f"\nNo '{transaction_type}'transactions recorded yet.")
                continue
            result=[t for t in self.Transactions if t.t_type == transaction_type] # follows the same principle as the filter by month method
            if result:
                self.display_results(result)
                return

    def filter_by_description(self): #uses the user's keywords and categories to filter transactions
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        recorded_descriptions = sorted({t.description for t in self.Transactions})
        print("\nRecorded descriptions available:", ", ".join(recorded_descriptions)) #displays which categories are available to filter
        while True:
            keyword = input("Enter keyword to search in descriptions: ").strip().lower()
            results = [
                t for t in self.Transactions
                if keyword in t.description.lower() # uses the .lower() to avoid inconsistencies between "Salary" and "salary" for example
            ]
            if results:
                self.display_results(results)
                return

    def _totals(self): # a helper function to make it easy to run the summarize budget functionality
        total_income = sum(t.amount for t in self.Transactions if t.t_type == "income") # does sum for all incomes recorded
        total_expense = sum(t.amount for t in self.Transactions if t.t_type == "expense") # does sum for all expenses recorded
        return total_income, total_expense

    def _per_category(self):
        cat = {}  # dictionary to store category totals: {category: {"earned": x, "spent": y}}
        for t in self.Transactions:
            # Use the transaction's description as the key; if missing, label as 'Uncategorized'
            key = t.description if t.description is not None else "Uncategorized"

            # Create category entry if not already present
            if key not in cat:
                cat[key] = {"earned": 0.0, "spent": 0.0}

            # Add amounts depending on transaction type
            if t.t_type == "income":
                cat[key]["earned"] += t.amount
            else:  # expense
                cat[key]["spent"] += t.amount

        return cat  # return the full category summary dictionary

    def summarize_Transactions(self):  # summarize all transactions
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return

        while True:
            # Display summary options
            print('1. Total Summary')
            print('2. Per-category Summary')
            print('3. Exit')

            choice = int(input("choose the summary you want: "))

            if choice == 1:
                # Compute total income + expenses
                total_income, total_expense = self._totals()
                balance = total_income - total_expense

                # Create summary table for display
                summary_table = [
                    ["Total Income", f"${total_income:.2f}"],
                    ["Total Expenses", f"${total_expense:.2f}"],
                    ["Balance", f"${balance:.2f}"],
                ]

                print("\n=== Budget Summary ===")
                print(tabulate(summary_table, tablefmt="fancy_grid"))

            elif choice == 2:
                # Get category breakdown
                cat = self._per_category()

                # Build table rows for display
                cat_rows = []
                for description, values in sorted(cat.items()):
                    cat_rows.append([description, f"${values['earned']:.2f}", f"${values['spent']:.2f}"])

                print("\nPer-category totals:")
                print(tabulate(cat_rows, headers=["Category", "Earned", "Spent"], tablefmt="grid"))

            elif choice == 3:
                print('returning to main menu')
                return

            else:
                # Handle invalid input
                print("Invalid choice! Please try again.")
                continue

    def set_threshold(self):
        print("\n--- Set Category Threshold ---")

        # category name converted to lowercase for consistent matching
        category = input("Enter category name: ").strip().lower()

        # ask for maximum allowed spending for that category
        amount = input("Enter max allowed spending amount: ")

        try:
            amount = float(amount)  # validate numeric value
        except ValueError:
            print("Invalid amount! Must be a number.")
            return

        # store the threshold in the dictionary
        self.thresholds[category] = amount
        print(f"Threshold set for '{category}' at ${amount}.")

    def check_threshold_warning(self, description):
        # If category has no threshold, nothing to check
        if description not in self.thresholds:
            return

        # Retrieve the spending limit
        limit = self.thresholds[description]

        # Calculate total amount spent for this category
        spent = sum(
            t.amount for t in self.Transactions
            if t.t_type == "expense" and t.description == description
        )

        # If user exceeded the limit
        if spent >= limit:
            print(f" WARNING: You have EXCEEDED your {description} budget (${limit})!")

        # If the user reached 80% of the limit
        elif spent >= 0.8 * limit:
            print(f" ALERT: You have reached 80% of your {description} budget (${limit}).")
