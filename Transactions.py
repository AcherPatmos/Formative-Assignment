class Transaction: #created the transaction class and assigned attributes
    def __init__(self, date, amount, description,t_type):
        self.date = date
        self.amount = amount
        self.description = description
        self.t_type = t_type

class Income(Transaction): # created the Income class that is inheriting from Transactions
    def __init__(self, date, amount, description):
        super().__init__(date,amount,description,'income')

class Expense(Transaction): #created the Expenses class inheriting from Transaction
    def __init__(self, date, amount, description):
        super().__init__(date,amount,description,'expense')
