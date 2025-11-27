from datetime import datetime, timedelta
from tabulate import tabulate
from Transactions import Income, Expense

class BudgetTracker:
    def __init__(self):
        self.Transactions=[]
        self.balance=0
        self.thresholds = {}

    def validate_date(self):
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

    def get_amount(self):
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

    def add_income(self):
        t_date = self.validate_date()
        amount= self.get_amount()
        description = input("enter transaction category(eg:Salary,Groceries): ").strip().lower()
        inc=Income(t_date,amount,description)
        self.Transactions.append(inc)
        self.balance+=amount
        print(f"transaction recorded successfully Current balance= ${self.balance}")

    def add_expense(self):
        t_date = self.validate_date()
        amount = self.get_amount()
        description = input("enter transaction category(eg:Salary,Groceries): ").strip().lower()
        exp=Expense(t_date,amount,description)
        self.Transactions.append(exp)
        self.balance-=amount
        self.check_threshold_warning(description)
        print(f"transaction recorded successfully Current balance= ${self.balance}")

    def list_transactions(self):
        if not self.Transactions:
            print("No transactions recorded yet.")
            return
        table=[]
        for x in self.Transactions:
            table.append([x.date,x.t_type.upper(),x.amount,x.description])
        headers=["Date","Type","Amount","Description"]
        print("Transactions list")
        print(tabulate(table,headers,tablefmt="fancy_grid"))
        print(f'current balance= ${self.balance}')

    def filter_transactions(self):
        print("choose one of the filter options below: ")
        print("1. filter by Date")
        print("2. filter by Transaction type")
        print("3. filter by description")
        print("4. exit")
        while True:
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

    def display_results(self, results):
        if not results:
            print("No matching transactions found")
            return
        table = [
            [x.date.strftime("%Y/%m"), x.t_type.upper(), x.amount, x.description]
            for x in results
        ]
        print("\nFiltered Results:")
        print(tabulate(table, ["Date", "Type", "Amount", "Description"], tablefmt="fancy_grid"))

    def filter_by_month(self):
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        recorded_months = sorted({t.date.strftime("%Y-%m") for t in self.Transactions})
        print("\nRecorded months to filter:", ", ".join(recorded_months))
        while True:
            dt = input("Enter a date (YYYY/MM): ")
            if len(dt) != 7 or dt[4] != "/":
                print("Invalid format! Use YYYY/MM (e.g., 2025/04).")
                continue
            results = [t for t in self.Transactions if t.date.strftime("%Y/%m") ==dt]
            if results:
                self.display_results(results)
                return
            print("Invalid month or no transactions in that month.")

    def filter_by_type(self):
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        recorded_types = sorted({t.t_type for t in self.Transactions})
        print("\nAvailable transaction types:", ", ".join(t.lower() for t in recorded_types))
        while True:
            transaction_type = input("Enter a transaction type(income/expense): ")
            if transaction_type not in ["income", "expense"]:
                print("\nInvalid type! Must be 'income' or 'expense'.")
                continue
            if transaction_type not in recorded_types:
                print(f"\nNo '{transaction_type}'transactions recorded yet.")
                continue
            result=[t for t in self.Transactions if t.t_type == transaction_type]
            if result:
                self.display_results(result)
                return

    def filter_by_description(self):
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        recorded_descriptions = sorted({t.description for t in self.Transactions})
        print("\nRecorded descriptions available:", ", ".join(recorded_descriptions))
        while True:
            keyword = input("Enter keyword to search in descriptions: ").strip().lower()
            results = [
                t for t in self.Transactions
                if keyword in t.description.lower()
            ]
            if results:
                self.display_results(results)
                return

    def _totals(self):
        total_income = sum(t.amount for t in self.Transactions if t.t_type == "income")
        total_expense = sum(t.amount for t in self.Transactions if t.t_type == "expense")
        return total_income, total_expense

    def _per_category(self):
        cat = {}
        for t in self.Transactions:
            key = t.description if t.description is not None else "Uncategorized"
            if key not in cat:
                cat[key] = {"earned": 0.0, "spent": 0.0}
            if t.t_type == "income":
                cat[key]["earned"] += t.amount
            else:  # expense
                cat[key]["spent"] += t.amount
        return cat

    def summarize_Transactions(self):
        if not self.Transactions:
            print("\nNo transactions recorded yet.\n")
            return
        while True:
            print('1. Total Summary')
            print('2. Per-category Summary')
            print('3. Exit')
            choice=int(input("choose the summary you want: "))
            if choice==1:
                total_income, total_expense = self._totals()
                balance = total_income - total_expense
                # summary table
                summary_table = [
                    ["Total Income", f"${total_income:.2f}"],
                    ["Total Expenses", f"${total_expense:.2f}"],
                    ["Balance", f"${balance:.2f}"],
                ]
                print("\n=== Budget Summary ===")
                print(tabulate(summary_table, tablefmt="fancy_grid"))
            elif choice==2:
                cat = self._per_category()
                # per-category table
                cat_rows = []
                for description, values in sorted(cat.items()):
                    cat_rows.append([description, f"${values['earned']:.2f}", f"${values['spent']:.2f}"])
                print("\nPer-category totals:")
                print(tabulate(cat_rows, headers=["Category", "Earned", "Spent"], tablefmt="grid"))
            elif choice==3:
                print('returning to main menu')
                return
            else:
                print("Invalid choice! Please try again.")
                continue

    def set_threshold(self):
        print("\n--- Set Category Threshold ---")

        category = input("Enter category name: ").strip().lower()
        amount = input("Enter max allowed spending amount: ")

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount! Must be a number.")
            return

        self.thresholds[category] = amount
        print(f"Threshold set for '{category}' at ${amount}.")

    def check_threshold_warning(self, description):
        if description not in self.thresholds:
            return  # No threshold set
        limit = self.thresholds[description]
        spent = sum(
            t.amount for t in self.Transactions
            if t.t_type == "expense" and t.description == description
        )
        if spent >= limit:
            print(f" WARNING: You have EXCEEDED your {description} budget (${limit})!")
        elif spent >= 0.8 * limit:
            print(f" ALERT: You have reached 80% of your {description} budget (${limit}).")

