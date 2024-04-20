# Подсчитать количество цифр в числе. Реализовать двумя видами циклов

number = int(input("number1: "))
count = 0

for a in str(number):
    count += 1

print(count)


number = int(input("number2: "))
count = 0

while number > 0:
    number //= 10
    count += 1

print(count)
