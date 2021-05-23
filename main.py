from my_functions import Account, ask_for_action, say_goodbye, print_help


myBalance = myExpense = myIncome = 0

myWallet = Account(myBalance, myExpense, myIncome)

while True:

    ask = ask_for_action()

    if ask == 0:
        myWallet.count_expenses()

    elif ask == 1:
        myWallet.count_income()

    elif ask == 2:
        say_goodbye()
        break

    elif ask == 3:
        print_help()

    elif ask == 4:
        print(myWallet.show_balance())
