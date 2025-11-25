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

    show_expenses()

def show_expenses():
    """Prints the expense list in a table format in the terminal,
    asks the user for an action and calls the corresponding function"""

    print(
        tabulate(
            expenses,
            headers=['Expense', 'Amount (€)', 'Date', 'Category'],
            tablefmt="fancy_grid",
            showindex="always",
            floatfmt=".2f"
        )
    )

    user_choice = str(input("\n What would you like to do? To add an expense, type 'add', to remove an expense, type 'remove', "
          "to calculate the total amount spent, type 'total' or to exit, type 'exit'.\n")).lower()
    functions[user_choice]()

# def remove_expense():
#
# def calculate_total():
#
# def save_file():
#
# def exit():

functions = {
    "add": add_expense,
}

if expenses:
    show_expenses()
else:
    add_expense()