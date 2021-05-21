from categories import expenses_list, income_list
from manage_db import save_to_db
import datetime


class Account:
    def __init__(self, balance, expense, income):
        self.balance = balance
        self.expense = expense
        self.income = income

    def count_expenses(self):

        category = input("Choose category of expense: ")
        # Get function name in order to save amount to correct column
        current_func = Account.count_expenses.__name__

        while category[:1].upper()+category[1:].lower() not in expenses_list:
            print_categories(current_func)
            category = input("Choose category from a list: ")

        name = input("Detailed name of expense: ")

        amount = int(input("Expense height: "))

        current_time = datetime.datetime.now()

        self.balance = self.balance - amount
        save_to_db(category, name, amount, current_time.strftime("%d/%m/%Y"), current_func)

    def count_income(self):

        category = input("Choose category of income: ")
        # Get function name in order to save amount to correct column
        current_func = Account.count_income.__name__

        while category[:1].upper() + category[1:].lower() not in income_list:
            print_categories(current_func)
            category = input("Choose category from an income list: ")

        name = input("Detailed name of income: ")

        amount = int(input("Income height: "))

        current_time = datetime.datetime.now()

        self.balance = self.balance + amount
        save_to_db(category, name, amount, current_time.strftime("%d/%m/%Y"), current_func)

    def show_balance(self):
        return "Your current balance is: {}".format(self.balance)


def print_categories(current_func):
    if current_func == "count_expenses":
        print("Printing list of categories: ")
        for item in expenses_list:
            print(item)
    else:
        print("Printing list of categories: ")
        for item in income_list:
            print(item)


def ask_for_action():
    choice = input("Type: expense or income or balance: ")
    if choice.lower() == "expense":
        return 0
    elif choice.lower() == "income":
        return 1
    elif choice.lower() == "q":
        return 2
    else:
        return 3


def say_goodbye():
    print("Goodbye!")