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

        amount = input("Expense height: ")
        validated_amount = input_validation(amount)

        current_time = datetime.datetime.now()

        self.balance = self.balance - validated_amount
        save_to_db(category, name, validated_amount, current_time.strftime("%d/%m/%Y"), current_func)

    def count_income(self):

        category = input("Choose category of income: ")

        # Get function name in order to save amount to correct column
        current_func = Account.count_income.__name__

        while category[:1].upper() + category[1:].lower() not in income_list:
            print_categories(current_func)
            category = input("Choose category from an income list: ")

        name = input("Detailed name of income: ")

        amount = input("Income height: ")
        validated_amount = input_validation(amount)

        current_time = datetime.datetime.now()

        self.balance = self.balance + validated_amount
        save_to_db(category, name, validated_amount, current_time.strftime("%d/%m/%Y"), current_func)

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

    choice = input("Type: expense, income, balance or help: ")

    if choice.lower() == "expense":
        return 0
    elif choice.lower() == "income":
        return 1
    elif choice.lower() == "q":
        return 2
    elif choice.lower() == "help":
        return 3
    else:
        return 4


def say_goodbye():
    print("Goodbye!")


def input_validation(user_input):
    while True:
        try:
            valid_input = float(user_input)
        except ValueError:
            user_input = input("Please enter float value: ")
            continue

        return float(valid_input)


def print_help():
    print("This is a wallet app to count your income and expenses.")
    print("You can use following options: ")
    print("- income  - to save and describe your income")
    print("- expense - to save and describe your expense")
    print("- q       - for quit")
    print("- balance - to check your account balance")
    print("Program starts with 0,00 amount on your account but all your input ")
    print("Is automatically saved to a database. So it is possible to see all your records.")
