# У Вас есть строка, состоящая из двух слов, разделенных пробелом.
# Переставьте эти слова местами.

a = "one two"
b = ' '.join(a.split()[::-1])
print(b)
