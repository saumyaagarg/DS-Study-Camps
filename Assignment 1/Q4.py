# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    def modulus(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

    def floor_divide(self, a, b):
        if b != 0:
            return a // b
        else:
            return "Error! Division by zero."

# Example usage
calc = Calculator()
print("Addition: 5 + 3 = ", calc.add(5, 3))
print()
print("Subtraction: 10 - 4 = ", calc.subtract(10, 4))
print()
print("Multiplication: 7 * 2 = ", calc.multiply(7, 2))
print()
print("Division: 8 / 2 = ", calc.divide(8, 2))
print()
print("Division: 8 / 0 = ", calc.divide(8, 0))
print()
print("Modulus: 10 % 3 = ", calc.modulus(10, 3))
print()
print("Power: 2 ^ 3 = ", calc.power(2, 3))
print()
print("Floor Division: 7 // 2 = ", calc.floor_divide(7, 2))