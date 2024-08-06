# Basic Calculator program that performs addition, subtraction,
# multiplication, and division based on user input.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Take input from the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Get the user's choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        # Get the two numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the chosen operation and print the result
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        
        # Ask if the user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid input")

print("Calculator closed.")
