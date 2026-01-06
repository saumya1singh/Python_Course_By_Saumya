print("Welcome to Expense Tracker")

expenses_list = []

while True:
    print("\n----- Menu -----")
    print("1. Add Expense(s)")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. View Category-wise Total")
    print("5. Edit/Update Expense")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input(("Please enter your choice number:"))

# Add Expense-----------
    if choice == "1":
        while True:
            Date = input("Enter Date (DD-MM-YYYY): ")
            Category = input("Enter Category (Food/Travel/Shopping/Other): ")
            Description = input("Enter Description: ")
            Amount = float(input("Enter Amount: "))

            expense = {
                "date": Date,
                "category": Category,
                "description": Description,
                "amount": Amount
            }

            expenses_list.append(expense)
            print("Expense added!")

            more = input("Add another expense? (yes/no): ").lower()
            if more != "yes":
                break


# View Expense-----------
    elif choice == "2":
        if len(expenses_list) == 0:
            print("No expenses found!")
        else:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses_list, start=1):
                print(
                    f"\nExpense {i}\n"
                    f"Date: {exp['date']}\n"
                    f"Category: {exp['category']}\n"
                    f"Description: {exp['description']}\n"
                    f"Amount: {exp['amount']}"
                )


# Total Expense----------
    elif choice == "3":
        if len(expenses_list) == 0:
            print("No expenses to calculate!")
        else:
            total = sum(e["amount"] for e in expenses_list)
            print(f"Your Total Expense is: {total}")


# Category-Wise Total---------
    elif choice == "4":
        if len(expenses_list) == 0:
            print("No expenses added yet!")
        else:
            category_totals = {}
            for exp in expenses_list:
                cat = exp["category"].capitalize()
                category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

            print("\nCategory-wise Totals:")
            for category, total in category_totals.items():
                print(f"{category}: {total}")


# Update Expense---------
    elif choice == "5":
        if len(expenses_list) == 0:
            print("No expenses to edit!")
        else:
            for i, exp in enumerate(expenses_list, start=1):
                print(f"{i}. {exp['description']} ({exp['amount']})")

            edit_index = int(input("Enter expense number to edit: ")) - 1

            if 0 <= edit_index < len(expenses_list):
                print("Leave field blank to keep existing value.")

                new_date = input(f"New Date ({expenses_list[edit_index]['date']}): ")
                if new_date:
                    expenses_list[edit_index]['date'] = new_date

                new_cat = input(f"New Category ({expenses_list[edit_index]['category']}): ")
                if new_cat:
                    expenses_list[edit_index]['category'] = new_cat

                new_desc = input(f"New Description ({expenses_list[edit_index]['description']}): ")
                if new_desc:
                    expenses_list[edit_index]['description'] = new_desc

                new_amt = input(f"New Amount ({expenses_list[edit_index]['amount']}): ")
                if new_amt:
                    expenses_list[edit_index]['amount'] = float(new_amt)

                print("Expense updated successfully!")
            else:
                print("Invalid selection!")


# Delete Expense----------
    elif choice == "6":
        if len(expenses_list) == 0:
            print("No expenses to delete!")
        else:
            for i, exp in enumerate(expenses_list, start=1):
                print(f"{i}. {exp['description']} ({exp['amount']})")

            del_index = int(input("Enter expense number to delete: ")) - 1

            if 0 <= del_index < len(expenses_list):
                deleted = expenses_list.pop(del_index)
                print(f"Deleted: {deleted['description']}")
            else:
                print("Invalid selection!")


# Exit----------
    elif choice == "7":
        print("Goodbye!")
        break


# Invailid Choice----------
    else:
        print("Invalid choice, try again!")
