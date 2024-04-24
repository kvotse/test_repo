class Person:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def age(self):
        current_year = 2024
        return current_year - self.birth_year


person = Person('kol', 'ufa', 2002)
print(person.age())
