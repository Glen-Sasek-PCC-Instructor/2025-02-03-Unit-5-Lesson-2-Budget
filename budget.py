



# Budget for a month USD: 1000.00
# Add expense USD [Q/q to quit]: 10
# Add expense USD [Q/q to quit]: 105
# Add expense USD [Q/q to quit]: 42
# Add expense USD [Q/q to quit]: 7
# Add expense USD [Q/q to quit]: 2000
# Add expense USD [Q/q to quit]: q
# EXPENSES: $2164.00
# BUDGET: $1000.00
# BALANCE: $(-1164.00)


DEBUG = True

budgetUSD = 0.00
sumExpenses = 0.00

budgetUSD = float(input("Budget for a month USD: "))

# https://docs.python.org/3/reference/compound_stmts.html#while
# https://wiki.python.org/moin/BeginnersGuide/Programmers/SimpleExamples?highlight=%28CategoryDocumentation%29
while True:
    expense = input("Add expense USD [Q/q to quit]: ")
    if DEBUG:
        print()
        print("DEBUG-->INPUT : ", expense)
        print()

    if expense.lower() == "q":
        break
    else:
        sumExpenses = sumExpenses + float(expense)
    
print("")
print("EXPENSES: $", sumExpenses)
print("BUDGET: $", budgetUSD)
print("BALANCE: $", budgetUSD - sumExpenses)


