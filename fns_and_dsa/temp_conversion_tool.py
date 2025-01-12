# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Convert a temperature from Fahrenheit to Celsius using the global conversion factor.
    
def convert_to_celsius(fahrenheit):
    
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Convert a temperature from Celsius to Fahrenheit using the global conversion factor.

def convert_to_fahrenheit(celsius):
    
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main function to interact with the user for temperature conversion.

def main():
    
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F.")
        elif unit == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()