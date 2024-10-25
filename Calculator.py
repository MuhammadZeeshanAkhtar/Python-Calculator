# Simple Calculator in Python 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select Operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        # Display result as integer if no decimal part, otherwise as float
        if result == int(result):
            print(f"The result is: {int(result)}")
        else:
            print(f"The result is: {result}")
        
    else:
        print("Invalid input! Please choose a valid option.")
        return

while True:
    calculator()
    # Asking the user if they want to perform another calculation
    Request = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if Request != 'yes':
        print("Goodbye!")
        break

    
