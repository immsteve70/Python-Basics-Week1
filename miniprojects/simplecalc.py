print("Welcome to A USUAL CALCULATOR!")
while True:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    print("Options\n1.Addtion\n2.Subraction\n3.Multiplication\n4.Division\n5.Exit")
    action = int(input("Enter the operation: "))

    if action == 1:
        add = num1 + num2
        print(f"Answer: {add}")
    elif action == 2:
        sub = num1 - num2
        print(f"Answer: {sub}")
    elif action == 3:
        mul = num1 * num2
        print(f"Answer: {mul}")
    elif action == 4:
        if num2 == 0:
            print("Error: cannot be divided by zero!")
        else:
            div = num1 / num2
            print(f"Answer: {div}")
    elif action == 5:
        print("Goodbyeee!! Thanks for using my calculator")
        break
    else:
        print("Invalid response!")
