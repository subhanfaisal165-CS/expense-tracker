from expense import add_expense, view_expenses, total_expenses, delete_expense
print("=== Expense Tracker ===")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
