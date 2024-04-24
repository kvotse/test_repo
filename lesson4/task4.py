class Kol:
    def __init__(self, word, number):
        self.word = word
        self.number = number

    def __str__(self):
        return f"word: {self.word}, number: {self.number}"


ya = Kol("Kolya", 22)
# 1
print(str(ya))
# 2
print(ya)
