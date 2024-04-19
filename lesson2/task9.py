# Соедините два списка и отсортируйте их. Затем удалите повторяющиеся элементы.

a = [4, 1, 4, 3, 2]
b = [5, 6, 6, 9, 8]
c = a + b
sorted_c = sorted(c)
upd_sorted_c = list(set(sorted_c))
print(upd_sorted_c)
