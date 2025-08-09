def calculator():
    print("Welcome to the Interactive Calculator!\n")

    while True:
        try:
        
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print(" +  Addition")
            print(" -  Subtraction")
            print(" *  Multiplication")
            print(" /  Division")

            operation = input("Enter operation (+, -, *, /): ").strip()

            if operation == '+':
                result = num1 + num2
                print(f"\n✅ Result: {num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"\n✅ Result: {num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"\n✅ Result: {num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("\n❌ Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"\n✅ Result: {num1} / {num2} = {result}")
            else:
                print("\n❌ Invalid operation. Please choose +, -, *, or /.")

        except ValueError:
            print("\n❌ Invalid input. Please enter numeric values.")

        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("\n👋 Thanks for using the calculator. Goodbye!")
            break

calculator()
