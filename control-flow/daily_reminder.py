 # Prompt for task description
while True:
    task = input("Enter your task: ")
    if task:
        break
    print("Task description cannot be empty!")

# Prompt for task priority
while True:
    priority = input("Enter your task's priority (high/medium/low): ")
    if priority in ["high", "medium", "low"]:
        break  # Exit the loop if the input is valid
    print("Invalid priority! Please enter 'high', 'medium', or 'low'.")
    
 # Prompt for time sensitivity
while True:
    time_bound = input("Is it time-bound? (yes/no): ")
    if time_bound in ["yes", "no"]:
        break  # Exit the loop if the input is valid
    print("Invalid response! Please enter 'yes' or 'no'.")

# Process the task based on priority using match case
match priority:
    case "high": 
        reminder = f"The task {task} has high priority."
    case "medium":
        reminder = f"The task {task} has medium priority."
    case "low":
        reminder = f"The task {task} has low priority."
    case _:
        reminder = f"The task {task} has an unspecified priority level."

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
    
else:
    reminder += " It can be scheduled to a later time today!"

# Provide a customized reminder
print(reminder)