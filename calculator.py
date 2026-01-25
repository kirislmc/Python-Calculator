operator: str = input("Which Operator you want to use? (+ - * /): ")

if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    num1: float = float(input("Enter the 1st Number: "))
    num2: float = float(input("Enter the 2nd Number: "))
    
    if operator == "+":
        summary: float = num1 + num2
        print(f"{num1} + {num2} = {round(summary, 2)}")

    elif operator == "-":
        summary: float = num1 - num2
        print(f"{num1} - {num2} = {round(summary, 2)}")

    elif operator == "*":
        summary: float = num1 * num2
        print(f"{num1} * {num2} = {round(summary, 2)}")

    elif operator == "/":
        summary: float = num1 / num2
        print(f"{num1} / {num2} = {round(summary, 2)}")

else:
    print(f"{operator} is an invalid operator!")
    