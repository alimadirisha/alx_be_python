# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Using a while loop to iterate through rows
while row < size:
    
    # Using a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
        
    print()  # Moves to the next line after completing the row
    
    row += 1   # Increments the row counter