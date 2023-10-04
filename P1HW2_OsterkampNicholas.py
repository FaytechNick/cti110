# Travel Expense Calculator
# Date- 10/3/2023
# CTI-110 P1HW2 - Travel Expense
# Nicholas Osterkamp

def budgetcalc():

    print("This program calculates and displays travel expenses")

    budget = float(input("Enter Budget: "))
    
    destination = input("Enter your travel destination: ")

    gas_expense = float(input("How much do you think you will spend on gas? "))

    accomodation_expense = float(input("Approximately, how much will you need for accomodation/hotel? "))

    food_expense = float(input("Last, how much do you need for food? "))

    total_expenses = gas_expense + accomodation_expense + food_expense

    remaining_budget = budget - total_expenses

    print("------------Travel Expenses------------")
    print("Location: " + str(destination))
    print("Initial Budget: " + str(budget))

    print("\nFuel: " + str(gas_expense))
    print("Accomodation: " + str(accomodation_expense))
    print("Food: " + str(food_expense))

    print("\nRemaining Balance: " + str(remaining_budget))

budgetcalc()

# Define Function budgetcalc

#     Print program introduction

#     Get budget from user
#     Get destination from user
#     Get gas_expense from user
#     Get accomodation_expense from user
#     Get food_expense from user

#     Calculate total_expenses as sum of gas_expense, accomodation_expense, and food_expense
#     Calculate remaining_budget by subtracting total_expenses from budget

#     Display all inputs and calculations

# Run Function budgetcalc