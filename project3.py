#Name: Ameya Deshpande
#project3

#expense tracker
import json
import matplotlib.pyplot as plt

# Define the categories
CATEGORIES = ["Rent", "Food", "Bills", "Clothes/Laundry", "Misc", "Health", "Investment"]

# Load expenses from file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Validate the expense input
def validate_input(amount: str, category: str):
    try:
        amount = float(amount)
        if category not in CATEGORIES:
            raise ValueError("That category doesn't seem to be in our list. Please choose one from the available options.")
    except ValueError as e:
        print(f"Something went wrong: {e}")
        return False
    return True

# Add an expense
def add_expense(expenses):
    print("\nLet's add a new expense!")
    amount = input("enter amount (in INR)? ₹")
    description = input("What was it for? (A brief description ): ")
    
    print("\nHere are the categories you can choose from:")
    print(", ".join(CATEGORIES))
    category = input("Which category does this expense belong to? (Choose from the list above): ")

    if validate_input(amount, category):
        expense = {"amount": float(amount), "description": description, "category": category}
        expenses.append(expense)
        print(f"\nGot it! Your expense has been recorded: {expense}")
        save_expenses(expenses)
    else:
        print("we couldn't add that expense. Please try again.")

# Show total expenditure for the month
def total_expenditure(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nYour total expenditure this month is: ₹{total:.2f}")

# Show summary of expenses by category
def category_summary(expenses):
    summary = {category: 0 for category in CATEGORIES}
    for expense in expenses:
        summary[expense['category']] += expense['amount']
    
    print("\nHere's a breakdown of your spending by category:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

    return summary

# Display pie chart for category-wise expenses
def display_pie_chart(expenses):
    summary = category_summary(expenses)
    
    # Filter out categories with no expenses
    categories = [category for category, amount in summary.items() if amount > 0]
    amounts = [amount for amount in summary.values() if amount > 0]

    if categories:
        plt.figure(figsize=(7, 7))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('How You Spent Your Money - Category Breakdown')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    else:
        print("\nLooks like you haven't spent in any categories yet. Add some expenses to see the chart!")

# Display the menu and prompt the user for their choice
def show_menu():
    print("\nWelcome to your Expense Tracker! What would you like to do today?")
    print("1. Add a new expense")
    print("2. View your total expenditure")
    print("3. View your category-wise spending")
    print("4. See a pie chart of your spending")
    print("5. Exit")

# Main function to run the program
def main():
    print("Welcome! Let's get started with your Expense Tracker.")
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Please enter the number corresponding to your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            total_expenditure(expenses)
        elif choice == '3':
            category_summary(expenses)
        elif choice == '4':
            display_pie_chart(expenses)
        elif choice == '5':
            print("Thanks for using the Expense Tracker! Goodbye for now.")
            break
        else:
            print("Oops! That’s not a valid choice. Please pick a number between 1 and 5.")

if __name__ == "__main__":
    main()
