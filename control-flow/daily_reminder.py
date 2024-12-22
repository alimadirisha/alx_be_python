 # Prompt for task description
task = input("Enter your task description: ") 

# prompt for task priority
priority = input("Enter your task’s priority (high, medium, low): ")  

 # Prompt for time sensitivity
time_bound = input("is it time-bound? (yes or no): ") 
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