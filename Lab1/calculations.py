def calculate(operand1, operand2, operator):
    if operator == "add":
        return operand1 + operand2
    elif operator == "sub":
        return operand1 - operand2
    elif operator == "mult":
        return operand1 * operand2
    elif operator == "div":
        return operand1 / operand2

    raise Exception("Incorrect input. There's no such operand")


def find_even(my_list):
    my_even_list = list()

    for i in my_list:
        if i % 2 == 0:
            my_even_list.append(i)

    print(my_even_list)
