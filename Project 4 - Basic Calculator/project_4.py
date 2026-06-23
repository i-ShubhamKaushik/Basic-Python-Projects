# PROJECT 4 - BASIC CALCULATOR

num1= float(input("Enter first num: "))
op = input("Which operation do you want to perform? (+, -, *, /): ")
num2= float(input("Enter second num: "))

if op == "-":
    print(f"Result: {num1-num2}")
elif op == "+":
    print(f"Result: {num1+num2}")
elif op == "*":
    print(f"Result: {num1*num2}")
elif op == "/":
    if not(num2==0):
        print(f"Result: {num1/num2}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operation..!")