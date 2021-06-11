class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        print("Result:", (num1 + num2))

    def subtract(self, num1, num2):
        print("Result:", (num1 - num2))

    def multiply(self, num1, num2):
        print("Result:", (num1 * num2))

    def divide(self, num1, num2):
        print("Result:", (num1 / num2))


cal = Calculator()
print("Let’s Calculate!")
x = int(input())
z = input()
y = int(input())
print("Value 1:", x)
print("Operator:", z)
print("Value 2:", y)


if z == "+":
    cal.add(x, y)
elif z == "-":
    cal.subtract(x, y)
elif z == "*":
    cal.multiply(x, y)
else:
    cal.divide(x, y)
