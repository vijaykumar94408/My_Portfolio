# taken one emptylist to store list of tuples from user 
expenses = []
categories = set()   #stores categories from list and remove duplicates categories 

# defined a function  
def add_expense():
    try:
        # used try catch method to catch run time errors 


        # inputs from user 
        name = (input("Enter the expense name: "))
        amount = float(input("Enter the amount: "))
        category = input("Enter the category Frome Below FOOD, TRAVEL, ENTERTAINMENT AND EMI: ").upper()
        
        # Add the expense as a tuple (name, amount, category)
        expense_entry = (name, amount, category)
        
        # Append the expense to the list
        expenses.append(expense_entry)
        
        # Add the category to the set of categories
        categories.add(category)
        
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")

# Function to display a summary of expenses by category
def expense_summary():
    try:
        #if no expenses are added,this block will execute
        if len(expenses) == 0:
            print("No expenses to display.")
            return
        
        # Create a dictionary that summarizes expenses by category using dictionary comprehension
        summary = {category: sum(expense[1] for expense in expenses if expense[2] == category) for category in categories}
        print(summary)
        print("\nExpense Summary by Category:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Looping until user want to exit 
while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expense Summary")
    print("3. Exit")
    
    choice = input("Choose an option: ")  #user can able to choose the operation 
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        expense_summary()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
