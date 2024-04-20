# Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов

n = int(input("N: "))
summ = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        summ += i

print(summ)


N = int(input("N2: "))
summ = 0
j = 1

while j <= N:
    if j % 2 == 0:
        summ += j
    j += 1

print(summ)

