# Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]

a = input("string: ")
length = len(a)
reversed_string = ""

for i in range(length - 1, -1, -1):
    reversed_string = reversed_string + a[i] + ' '

print(reversed_string)

