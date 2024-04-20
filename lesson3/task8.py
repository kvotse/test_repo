# Определить, содержит ли список дубликаты

list1 = [1, 1, 3, 4, 5]
compare = len(list1) != len(set(list1))

if compare:
    print("yas, there is ")
else:
    print("no, there ins't")
