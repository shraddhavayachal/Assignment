def calculator():
    n1 = float(input("Enter your  First number: "))
    n2 = float(input("Enter your Second number: "))
    operator = input("Enter the Operator (+, -, *, /, %): ")

    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '/':
        result = n1 / n2
    elif operator == '%':
        result = n1 % n2
    else:
        print("Invalid Operator!")
        return
    print("Result:", result)
    process=input("press c to continue:")
    if process=="c":
        calculator()
    else:
        exit()
calculator()
