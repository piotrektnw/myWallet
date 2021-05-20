from my_functions import Account, ask_for_action

myBalance = 0
myExpense = int(input("Expense: "))
myIncome = int(input("Income: "))

myWallet = Account(myBalance, myExpense, myIncome)

while True:
    ask = ask_for_action()

    if ask == 0:
        myWallet.count_expenses()

    elif ask == 1:
        myWallet.count_income()

    elif ask == 2:
        print(myWallet.show_balance())


print(myWallet.show_balance())
