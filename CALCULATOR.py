def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Prompt user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Prompt user to choose an operation
choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user's choice
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    result = "can not devide by zero"
    result = "invalid input"

# Display the result
print("Result:", result) 