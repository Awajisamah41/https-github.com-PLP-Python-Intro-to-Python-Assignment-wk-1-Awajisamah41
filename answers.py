
# A simple calculator program that performs basic arithmetic operations.

# Function to perform the calculation.
def calculate(num1, num2, operator):
    """
    Performs a mathematical operation on two numbers based on the operator.
    Handles division by zero and invalid operators.
    """
    try:
        # Check the operator and perform the corresponding calculation.
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero.
            if num2 == 0:
                return "Error: Cannot divide by zero."
            result = num1 / num2
        else:
            return "Error: Invalid operator. Please use +, -, *, or /."

        # Return the formatted result string.
        return f"{num1} {operator} {num2} = {result}"
        
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Main part of the program.
def main():
    """
    Prompts the user for two numbers and an operator, then prints the result.
    """
    print("Welcome to the simple Python calculator!")

    # Use a try-except block to handle potential errors in input.
    try:
        # Get the first number from the user and convert it to a float.
        num1 = float(input("Enter the first number: "))
        
        # Get the second number from the user and convert it to a float.
        num2 = float(input("Enter the second number: "))
        
        # Get the operator from the user.
        operator = input("Enter the operation (+, -, *, /): ")
        
        # Call the calculate function and print the result.
        print(calculate(num1, num2, operator))
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main function when the script is executed.
if __name__ == "__main__":
    main()

