 # Prompt for task description
Task = input("Enter your task: ")
if not Task:
    print("Task description cannot be empty!")
print()

# Prompt for task priority
Priority = input("Enter your task's priority (high/medium/low): ")
if Priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter 'high', 'medium', or 'low'.")
print()
    
 # Prompt for time sensitivity
Time_bound = input("Is it time-bound? (yes/no): ")
if Time_bound not in ["yes", "no"]:
    print("Invalid response! Please enter 'yes' or 'no'.")
print()

# Process the task based on priority using match case
match Priority:
    case "high": 
        reminder = f"The task {Task} has high priority."
    case "medium":
        reminder = f"The task {Task} has medium priority."
    case "low":
        reminder = f"The task {Task} has low priority."
    case _:
        reminder = f"The task {Task} has an unspecified priority level."

# Modify the reminder based on time sensitivity
if Time_bound == "yes":
    reminder += " It requires immediate attention today!"
    
else:
    reminder += " It can be scheduled to a later time today!"

# Provide a customized reminder
print(reminder)