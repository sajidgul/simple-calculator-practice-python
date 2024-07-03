def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    Should_continue = True

    while Should_continue:
        operation_symbol = input("Pick an operation you want to do! ")
        num2 = float(input("Enter the second number: "))
        operation = operations[operation_symbol]
        answer = operation(num1, num2)
        print(f"the answer of {num1} {operation_symbol} {num2} is {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            Should_continue = False
            calculator()


calculator()

