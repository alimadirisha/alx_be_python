 # Prompt for task description
task = input("Enter your task: ")
if not task:
    print("Task description cannot be empty!")
    exit()

# prompt for task priority
priority = input("Enter your task's priority (high/medium/low): ")
if priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter 'high', 'medium', or 'low'.")
    exit()

 # Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ")
if time_bound not in ["yes", "no"]:
    print("Invalid response! Please enter 'yes' or 'no'.")
    exit()

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