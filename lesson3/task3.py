# Расчет факториала числа с выводом каждого шага

number = int(input("number: "))
result = 1

for i in range(1, number + 1):
    result *= i
    print(f"{i}:  {i}! = {result}")
