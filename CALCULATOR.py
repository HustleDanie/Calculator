def calculator():
    while True:
        print("Enter operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice == 5:
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
            print("Result:", result)
        elif choice == 2:
            result = num1 - num2
            print("Result:", result)
        elif choice == 3:
            result = num1 * num2
            print("Result:", result)
        elif choice == 4:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Invalid Input")

calculator()
