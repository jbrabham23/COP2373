# Jadyn Brabham Chapter 3 Assignment 3

# This program will ask the user for the amount and type of their monthly
# expenses. It will then analyze the expenses, and display the total
# expense, the highest expense, and the lowest expense.

from functools import reduce

# Function to calculate the total expense
def total_expense(expenses):
    return reduce(lambda acc, expense: acc + expense[1], expenses, 0)

# Function to find the highest expense
def highest_expense(expenses):
    return reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc,
                  expenses)

# Function to find the lowest expense
def lowest_expense(expenses):
    return reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc,
                  expenses)

# The main function asks the user for input, processes the input,
# and displays the total, highest, and lowest expense.
def main():
    expenses = []

    print("Please enter your monthly expenses.")

    while True:
        expense_type = input("Enter the type of expense or type done"
                             " to finish: ")
        if expense_type.lower() == 'done':
            break

        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

    if not expenses:
        print("No expenses were entered.")
        return

    total = total_expense(expenses)
    highest = highest_expense(expenses)
    lowest = lowest_expense(expenses)

    print(f"\nTotal expense: ${total:.2f}")
    print(f"\nHighest expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"\nLowest expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()