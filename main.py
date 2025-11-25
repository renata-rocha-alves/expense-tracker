from tabulate import tabulate
from art import logo

expenses = []
categories = ['Food', 'Transport', 'Entertainment', 'Healthcare', 'Other']

print(logo)
print("Welcome to your expense tracker")

def add_expense():
    """Asks the user for expense name, amount, date and category and adds it to the expense list"""

    expense = str(input("What did you spend? \n"))
    amount = float(input("How much did you spend?\n€ "))
    date = str(input("When did you spend it? Please use the format DD/MM/YYYY\n"))
    category = str(input(f"What category did you spend it in? Please select: {", ".join(categories)} \n")).title()

    expenses.append([expense, amount, date, category])
    print(f"\nExpense added successfully!\n")

    show_expenses()

def show_expenses():
    """Prints the expense list in a table format in the terminal,
    asks the user for an action and calls the corresponding function"""

    if not expenses:
        user_choice = str(input("You don't have any expenses saved yet. Would you like to add one? Type 'Y' to add or 'N' to exit.\n")).lower()
        if user_choice == "y":
            add_expense()
        else:
            exit_program()

    print(
        tabulate(
            # creates a dynamic id starting with 1 for each expense to be displayed in the table
            [[i + 1] + expense for i, expense in enumerate(expenses)],
            headers=['Expense', 'Amount (€)', 'Date', 'Category'],
            tablefmt="fancy_grid",
            floatfmt=".2f"
        )
    )

    next_action = str(input("\nWhat would you like to do? To add an expense, type 'add', to remove an expense, type 'remove', "
          "to calculate the total amount spent, type 'total' or to exit, type 'exit'.\n")).lower()
    functions[next_action]()

def remove_expense():
    """Removes the expense at the specified index from the expense list"""

    user_choice = str(input("Which expense would you like to remove? Type the number of the row or 'cancel' to cancel.\n"))
    if user_choice == "cancel":
        show_expenses()
    else:
        index = int(user_choice) - 1
        expenses.pop(index)
        print(f"Expense removed successfully!")
        show_expenses()

# def calculate_total():
#
# def save_file():
#
def exit_program():
    print("Thanks for using Expense Tracker!")

functions = {
    "add": add_expense,
    "remove": remove_expense,
    "exit": exit_program,
}

if expenses:
    show_expenses()
else:
    add_expense()