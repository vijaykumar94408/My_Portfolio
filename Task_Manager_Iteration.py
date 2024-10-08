    tasks = []   # taking a empty list to store task name and due date 


# defined a function to add tasks with task name and due date 
def add_task(task_name, due_date):
    task = (task_name, due_date, False)
    tasks.append(task)# every task from user added to empty list by append method 
    print(f"Task '{task_name}' added successfully.")


# defined a function to mark task as completed
def complete_task(task_index):
    try:
# implemented try except method to catch run time errors
        # while selecting to mark a task as complete, index is taking from 1 
        task_index -= 1  
        task_name, due_date, _ = tasks[task_index]
        tasks[task_index] = (task_name, due_date, True)
        print(f"Task '{task_name}' marked as completed.")
    except IndexError:
        print("Error: Task index is out of range. Please try again.")
# function defined to remove tasks 
def remove_task(task_index):
    try:
        task_index -= 1  
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task[0]}' removed successfully.")
    except IndexError:
        print("Error: Task index is out of range. Please try again.")
 # defined function to display the task 
def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    
    print("\nTask List:")
    for i, (task_name, due_date, status) in enumerate(tasks, 1):
        status_str = "Completed" if status else "Incomplete"
        print(f"{i}. Task: {task_name}, Due: {due_date}, Status: {status_str}")
    print()




# here i defined a function which take above function calling is implemented in every chosed function block 
def task_manager():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")
        # implemented try except method 
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        if choice == 1:
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (e.g., 2023-12-31): ")
            add_task(task_name, due_date)
        elif choice == 2:
            display_tasks()
            if tasks:
                try:
                    task_index = int(input("Enter task index to mark as complete: "))
                    complete_task(task_index)
                except ValueError:
                    print("Error: Please enter a valid number.")
        elif choice == 3:
            display_tasks()
            if tasks:
                try:
                    task_index = int(input("Enter task index to remove: "))
                    remove_task(task_index)
                except ValueError:
                    print("Error: Please enter a valid number.")
        elif choice == 4:
            display_tasks()
        elif choice == 5:
            print("Exiting the task manager. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select between 1 and 5.")
# calling function 
task_manager()
