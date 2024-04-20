# Проверить, является ли строка палиндромом (зеркальная)

a = input("word: ")

if a == a[::-1]:
    print("yas")
else:
    print("no")
