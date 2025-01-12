from datetime import datetime, timedelta


#Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
def display_current_datetime():
    
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

#Calculate and display the date after a specified number of days.
def calculate_future_date():
    
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"The date after {days_to_add} days will be: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate and display a future date
    calculate_future_date()