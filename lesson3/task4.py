# Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()

list1 = ['1', '2', '3', '1', '2', '3', '1']

for index, value in enumerate(list1):
    if (index + 1) % 3 == 0:
        print(index, value)
