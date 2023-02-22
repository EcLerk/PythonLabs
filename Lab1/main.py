from calculations import calculate

print("Task1")
print("Hello, world!")

print("\nTask2")
try:
    operand1 = float(input("Enter first number: "))
    operand2 = float(input("Enter second number: "))
    operator = input("Enter operator: ")
except ValueError:
    print("Incorrect input. Not a number")

print(calculate(operand1, operand2, operator))

print("\nTask3")



