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
