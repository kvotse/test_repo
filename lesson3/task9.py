# Удалить все дубликаты из списка без использования дополнительных структур.
# Реализовать двумя видами циклов, для удаления можно использовать pop() либо del

list1 = [1, 2, 3, 1, 4, 5, 2, 6, 2]
n = len(list1)

for i in range(n):
    j = i + 1
    while j < n:
        if list1[i] == list1[j]:
            list1.pop(j)
            n -= 1
        else:
            j += 1

print(list1)


list1 = ['a', 'a', 'b', 'c', 'd', 'd', 'e', 'e', 'f', 'f']
n = len(list1)
i = 0

while i < n:
    j = i + 1
    while j < n:
        if list1[i] == list1[j]:
            del list1[j]
            n -= 1
        else:
            j += 1
    i += 1

print(list1)
