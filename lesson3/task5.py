# Напечатать таблицу умножения для числа n, использовать f строки

n = int(input("number: "))

print("multiplying of number {n}:")
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
