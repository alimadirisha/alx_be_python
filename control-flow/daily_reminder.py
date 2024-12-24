 # Prompt for task description
Task = input("Enter your task: ")

# Prompt for task priority
Priority = input("priority(high/medium/low): ")

 # Prompt for time sensitivity
Time_bound = input("Is it time-bound? (yes/no): ")

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
    reminder += " Reminder: '{Task}' is a high priority task that requires immediate attention today!"
    
else:
    reminder += "Note: '{Task}' is a low priority task. Consider completing it when you have free time."

# Provide a customized reminder
print(reminder)