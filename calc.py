def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation!"

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        operation = input("Enter an operation (+, -, *, /): ")
        
        result = calculate(num1, num2, operation)
        
        print(f"The result is: {result}")
    
    except ValueError:
        print("Error! Please enter a valid number.")
calculator()
