 # Prompt for task description
Task = input("Enter your task: ")

# Prompt for task priority
Priority = input("priority(high/medium/low): ")

 # Prompt for time sensitivity
Time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using match case
match Priority:
    case "high": 
        level = f"is a high priority task."
    case "medium":
        level = f"is a medium priority task."
    case "low":
        level = f"is a low priority task."

# Modify the reminder based on time sensitivity
if Time_bound == "yes":
    print()
    print("Reminder: '{Task}' {leve} that requires immediate attention today!")
    
else:
    print()
    print("Note: '{Task}' '{level}'. Consider completing it when you have free time.")
