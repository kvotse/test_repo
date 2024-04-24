class Calculator:
    def summ(self, x, y):
        return x + y

    def unsumm(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "error"
        return x / y


calc = Calculator()

x = float(input("x: "))
y = float(input("y: "))

print("results")
print("+: ", calc.summ(x, y))
print("-: ", calc.unsumm(x, y))
print("*: ", calc.multiply(x, y))
print("/: ", calc.divide(x, y))
