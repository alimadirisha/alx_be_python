def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

result1 = perform_operation(3, 3, "add")
print(result1)

result2 = perform_operation(3, 1, "subtract")
print(result2)

reuslt3 = perform_operation(2, 2, "multiply")
print(reuslt3
      )
result4 = perform_operation(9, 0, "divide")
print(result4)
    
    
    
