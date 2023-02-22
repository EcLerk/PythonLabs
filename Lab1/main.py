from calculations import calculate, find_even

###########################################
print("Task1")
print("Hello, world!")

###########################################
print("\nTask2")
try:
    operand1 = float(input("Enter first number: "))
    operand2 = float(input("Enter second number: "))
    operator = input("Enter operator: ")

    print(calculate(operand1, operand2, operator))
except ValueError:
    print("Incorrect input. Not a number")

#############################################
print("\nTask3")

try:
    my_list = list(map(int, input("Enter the list: ").split()))

    find_even(my_list)
except ValueError:
    print("Incorrect input")




