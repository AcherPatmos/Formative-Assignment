# Budget Tracker

## Overview
BudgetTracker is a simple, beginner-friendly Python console application designed to help users manage their money, track their income and expenses, filter transactions, and receive warnings when they exceed a defined spending threshold. This project uses Object-Oriented Programming (OOP) principles, classes, inheritance, and external libraries like tabulate to display clean tables and timedelta for date validations.
All data is stored in memory for the duration of the session (no file I/O).

## Files

**BudgetTracker.py**  --Contains the BudgetTracker class and all program logic

**Transactions.py**   --Contains Transaction, Income, and Expense classes

**main.py**           --Main menu + program loop 

**tests.py**          --Basic test assertions for core functionality (optional)


## Features

- Add transactions: date, amount, category, description, and type (income/expense).
- List transactions in a readable table.
- Filter transactions by type, category, or month (YYYY-MM).
- set threshold amounts for expenses
- Summary: total income, total expenses, balance, and per-category totals.
- Input validation: enforces date format, numeric positive amounts, valid menu choices, and valid name user inputs.
- Session-only: no saving or loading to files — data remains in memory.

## Running

1. Ensure you have Python 3 installed.
2. Clone or download this repository.
3. Navigate to the project directory in your terminal.
4. install required dependencies
   ```bash
   pip install tabulate
   ```
6. Run the program:
   ```bash
   python main.py (py main.py for window users)
   ```
7. Follow the on-screen menu to add transactions, view summaries, and filter data.

## Requirements

- Python 3.x
- User has to install the tabulate library

## Project Structure

```
.
├── BudgetTracker.py
├── main.py
├── Transactions.py
├── Basic_Test.py
├── README.md
├── Project Reflection.txt
└── Project Screenshots/
```
# Sample Interactions

## Adding Income
welcome to your BudgetTracker!

please enter your name: Acher

Hello Acher let's get started with your budget tracking!

choose one of the options below
1. add income
2. add expenses
3. list transactions
4. filter transactions
5. summarize transactions
6. Set Transaction Threshold
0. exit

enter your choice: 1

Enter transaction date (DD/MM/YYYY): 20/04/2025

Enter amount: 1500

Enter transaction category(eg:Salary,Groceries): salary

transaction recorded successfully Current balance= $1500.0

## List Transactions
enter your choice: 3

│ Date       │ Amount   │ Type  │ Description │

│ 20/04/2025 │ 1500.00 │ income │ salary │

# Basic Test Assertions

These simple tests verify that adding income, adding expenses, and computing the balance work correctly.

(Tests are stored in a separate test file)
# Notes

What I learned: basic OOP in Python, building a user-friendly CLI, and careful input validation.
Future Improvement: storing user's data, adding in data visualization features
# Author
Patmos Acher Mpakaniye
