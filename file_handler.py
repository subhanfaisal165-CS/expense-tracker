import json


def load_expenses():
    with open("expenses.json", "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
