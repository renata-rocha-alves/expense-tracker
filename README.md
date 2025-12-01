# 💰 Expense Tracker

A simple and efficient Python command-line interface (CLI) application to help you track your daily spending.

## 📋 Features

- **Add Expenses**: Record expense details including name, amount, date, and category.
- **View Expenses**: Displays your spending list in a clean, professional table format (using `tabulate`).
- **Remove Expenses**: Easily delete items by selecting their ID number from the table.
-**Calculate Total**: Calculate total spent on all categories.
-**Save Expenses**: Save your expenses to a local JSON file for persistent storage.

## 🛠️ Installation

1. **Clone the repository** to your local machine.

2. **Install the required packages**:
   This project uses `tabulate` for table formatting. You can install it using the provided requirements file:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Run

Execute the `main.py` file from your terminal:

   ```bash
   python main.py
   ```

## 🕹️ Usage

Once the program starts, you will see the ASCII art logo and your current list of expenses (if any). You can type the following commands when prompted:

*   `add`: Start the process to add a new expense.
*   `remove`: Delete an existing expense by its ID.
*   `view`: View your entire list of expenses.
*   `total`: Calculate total spent.
*   `save`: Save your expenses to a local JSON file.
*   `exit`: Close the program.

## 📂 Project Structure

*   `main.py`: The core logic and entry point of the application.
*   `art.py`: Contains the ASCII art logo used in the welcome screen.
*   `expense_tracker.py`: Contains the logic for managing expenses.
*   `requirements.txt`: List of external Python dependencies.