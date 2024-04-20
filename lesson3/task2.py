# Найти самое длинное слово из массива. Реализовать двумя видами циклов

words = input("1 list:").split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)


words = input("2 list: ").split()
longest_word = ""
i = 0

while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
    i += 1

print(longest_word)
