class Account:
    def __init__(self, balance, expense, income):
        self.balance = balance
        self.expense = expense
        self.income = income

    def count_expenses(self):
        self.balance = self.balance - int(input("Expense height: "))

    def count_income(self):
        self.balance = self.balance + int(input("Income height: "))

    def show_balance(self):
        return "Your current balance is: {}".format(self.balance)


def ask_for_action():
    choice = input("Type: expense or income or balance: ")
    if choice.lower() == "expense":
        return 0
    elif choice.lower() == "income":
        return 1
    else:
        return 2