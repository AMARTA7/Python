# Write a Python programme to build a calculator.

# Functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select what operation you want to do:")
print(f"1.for Add")
print(f"2.for Subtract")
print(f"3.for Multiply")
print(f"4.for Divide")

while True:
    choice = input(f"Choice only (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input(f"Enter first number: "))
        num2 = float(input(f"Enter second number: "))

        if choice == '1':
            print(num1,"+",num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1,"-",num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1,"*",num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1,"/",num2, "=", divide(num1, num2))
        break
    else:
        print(f"You have to choice only (1/2/3/4):!!")
