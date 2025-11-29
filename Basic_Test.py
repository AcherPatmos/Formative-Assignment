from BudgetTracker import BudgetTracker, Income, Expense
# Import the classes exactly as your program uses them

def test_add_income():
    # Create a fresh BudgetTracker object for the test
    tracker = BudgetTracker()

    # Add an income transaction (directly providing the object)
    tracker.add_income(Income("20/04/2025", 1000, "Salary"))

    # The balance should now be 1000, because we started at 0
    assert tracker.balance == 1000

def test_add_expense():
    # Create a fresh tracker for isolation
    tracker = BudgetTracker()

    # Add an expense transaction
    tracker.add_expense(Expense("03/02/2025", 200, "Groceries"))

    # The balance should now be -200 (because 0 - 200)
    assert tracker.balance == -200

def test_balance_after_mixed_transactions():
    # Create tracker
    tracker = BudgetTracker()

    # Add income and expense
    tracker.add_income(Income("20/04/2025", 1000, "Salary"))
    tracker.add_expense(Expense("03/02/2025", 200, "Groceries"))

    # Balance should be 800
    assert tracker.balance == 800
