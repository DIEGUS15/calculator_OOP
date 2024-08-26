class Calculator:
    def __init__(self):
        pass

    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "error: Division by zero not allowed."

    def exponentiation(self, a, b):
        return a ** b


def main():
    calc = Calculator()

    print("Welcome to the Python OOP Calculator")
    print("Select the operation you wish to perform:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")

    option = int(input("Enter the operation number: "))

    if option in [1, 2, 3, 4, 5]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == 1:
            print(f"Result: {calc.sum(num1, num2)}")
        elif option == 2:
            print(f"Result: {calc.subtract(num1, num2)}")
        elif option == 3:
            print(f"Result: {calc.multiply(num1, num2)}")
        elif option == 4:
            print(f"Result: {calc.divide(num1, num2)}")
        elif option == 5:
            print(f"Result: {calc.exponentiation(num1, num2)}")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
