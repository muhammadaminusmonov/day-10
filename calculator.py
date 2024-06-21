import art


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate():
    print(art.logo)
    number1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        pick_operation = input("Chose the operation: ")
        calculation_function = operations[pick_operation]

        number2 = float(input("Enter the next number: "))
        answer = calculation_function(number1, number2)
        print(f"{number1} {pick_operation} {number2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if should_continue == "y":
            number1 = answer
        else:
            should_continue = False
            calculate()
    calculate()


calculate()
