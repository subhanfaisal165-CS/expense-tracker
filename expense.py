from file_handler import load_expenses, save_expenses


def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    expense = {
        "name": name,
        "amount": amount
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print(f"Expense added: {name} - Rs. {amount}")
    print("Expense saved successfully!")


def view_expenses():
    expenses = load_expenses()

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - Rs. {expense['amount']}")


def total_expenses():
    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses: Rs. {total}")


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    choice = int(input("Enter expense number to delete: "))

    deleted = expenses.pop(choice - 1)
    save_expenses(expenses)

    print(f"{deleted['name']} deleted successfully!")