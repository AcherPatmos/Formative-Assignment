class Transaction:
    def __init__(self, date, amount, description,t_type):
        self.date = date
        self.amount = amount
        self.description = description
        self.t_type = t_type

class Income(Transaction):
    def __init__(self, date, amount, description):
        super().__init__(date,amount,description,'income')

class Expense(Transaction):
    def __init__(self, date, amount, description):
        super().__init__(date,amount,description,'expense')
