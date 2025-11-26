import json

from art import logo
from tabulate import tabulate

expenses = []
categories = ['Food', 'Transport', 'Entertainment', 'Healthcare', 'Other']

print(logo)
print("Welcome to your expense tracker!\n")

def get_valid_input(prompt, data_type):
    """Continuously asks for input until the input is valid and returns it as the specified data type"""

    while True:
        try:
            user_input = input(prompt)
            return data_type(user_input)
        except ValueError:
            print(f"\nInvalid input. Please try again.\n")

def add_expense():
    """Asks the user for expense name, amount, date and category and adds it to the expense list"""

    expense = get_valid_input("\nWhat did you spend? \n", str)
    amount = get_valid_input("How much did you spend?\n€ ", float)
    date = get_valid_input("When did you spend it? Please use the format DD/MM/YYYY\n", str)
    category = get_valid_input(f"What category did you spend it in? Please select or type a new one: {", ".join(categories)} \n", str)

    expenses.append([expense, amount, date, category])
    print(f"\nExpense added successfully!")

    show_expenses()

def get_next_action():
    """Asks the user for the next action and calls the corresponding function"""

    if not expenses:
        print("\nYou don't have any expenses yet.")
        user_choice = get_valid_input("Type 'add' to add an expense, 'save' to save or 'exit' to exit.\n", str)

        if user_choice in ["add", "save", "exit"]:
            functions[user_choice]()
        else:
            print(f"\nInvalid action. Please try again.\n")
            get_next_action()

    next_action = str(
        input("\nWhat would you like to do?"
              "\nTo add an expense, type 'add'"
              "\nto remove an expense, type 'remove'"
              "\nto view your expenses, type 'view'"
              "\nto calculate the total amount spent, type 'total'"
              "\nto save your expenses, type 'save'"
              "\nor to exit, type 'exit'.\n")).lower()

    if next_action not in functions:
        print(f"\nInvalid action. Please try again.\n")
        get_next_action()

    functions[next_action]()

def show_expenses():
    """Prints the expense list in a table format in the terminal,
    asks the user for an action and calls the corresponding function"""

    if not expenses:
        get_next_action()

    print(f"\n{
        tabulate(
            # creates a dynamic id starting with 1 for each expense to be displayed in the table
            [[i + 1] + expense for i, expense in enumerate(expenses)],
            headers=['Expense', 'Amount (€)', 'Date', 'Category'],
            tablefmt="fancy_grid",
            floatfmt=".2f"
        )
    }")

    get_next_action()

def remove_expense():
    """Removes the expense at the specified index from the expense list"""

    user_choice = get_valid_input("\nWhich expense would you like to remove? Type the number of the row or 0 to cancel.\n", int)

    if user_choice == 0:
        show_expenses()
    elif user_choice - 1 in range(len(expenses)):
        index = user_choice - 1
        expenses.pop(index)

        print(f"\nExpense removed successfully!")
        show_expenses()
    else:
        print(f"\nInvalid choice. Please try again.\n")
        remove_expense()

def calculate_total():
    """Calculates the total amount spent and prints it in the terminal"""

    total = 0
    for item in expenses:
        total += item[1]

    print(f"\nYour total expenses are € {total:.2f}.")
    get_next_action()

def save_file():
    """Saves the expense list to a JSON file"""

    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

    print("\nExpenses saved successfully!")
    get_next_action()


def exit_program():
    """Exits the program and displays a thank-you message in the terminal"""

    print("\nThanks for using Expense Tracker!")
    exit()

functions = {
    "add": add_expense,
    "remove": remove_expense,
    "view": show_expenses,
    "total": calculate_total,
    "save": save_file,
    "exit": exit_program,
}

try:
    # Checks if there are any expenses saved in the JSON file, otherwise adds an expense
    with open("expenses.json", "r") as file:
        expenses.extend(json.load(file))

    if len(expenses) > 0:
        print("\nThese are your current expenses:")
        show_expenses()
    else:
        get_next_action()
except FileNotFoundError:
    get_next_action()