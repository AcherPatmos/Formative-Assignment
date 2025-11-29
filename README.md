# BudgetTracker – Personal Finance Management (Command-Line Application)

BudgetTracker is a simple, beginner-friendly Python console application designed to help users manage their money, track their income and expenses, filter transactions, and receive warnings when they exceed a defined spending threshold.
This project uses Object-Oriented Programming (OOP) principles, classes, inheritance, and external libraries like tabulate to display clean tables and timedelta for date validations

# Project Structure

Acher_Prog1FormativeProject_F25/

│

├── BudgetTracker.py        # Contains the BudgetTracker class and all program logic

├── Transactions.py         # Contains Transaction, Income, and Expense classes

├── main.py                 # Main menu + program loop (user interface)

└── tests.py                # Basic test assertions for core functionality (optional)


# Core features

### Record transactions

Add income or expense entries with date, amount, category.

### List transactions

Show all recorded transactions in a neat table.

### Filter transactions

Filter by month (YYYY-MM), type (income/expense), or Category keyword.

### Summaries

Total Income, Total Expenses, Balance.

Per-category totals separated into earned and spent.

### Budget threshold warnings(optional feature implemented)

Set a spending limit per category and receive automatic alerts (80% and exceeded).


Input validation

Validates dates, numeric amounts, and menu choices.

# Instructions on Running the Program
Requirements: Python 3.8+ (should work on Python 3.6+).

From PowerShell or any other CLI in the project root run: py main.py

For macOS/Linux:
python3 main.py

# Menu
Add income

Add expense

List transactions

Filter (by category / type / month)

Show summary

Set Transaction Threshold

Exit

