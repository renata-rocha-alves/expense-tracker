import json

from art import logo
from expense_tracker import expenses, get_next_action

print(logo)
print("Welcome to your expense tracker!\n")

# Checks if there are any expenses saved in the JSON file and prints them,
# otherwise asks the user for the next action
try:
    with open("expenses.json", "r") as file:
        expenses.extend(json.load(file))

    get_next_action("view")
except FileNotFoundError:
    get_next_action()