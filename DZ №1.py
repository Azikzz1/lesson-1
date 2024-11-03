class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduse(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в городе {self.city}.")

    def is_adult(self):
        return self.age >= "18"

    def __str__(self):
        return f"Имя: {self.name}\n Возраст: {self.age}\n Город: {self.city}"


person_1 = Person(name="Aziret", age="17", city="Bishkek")
person_2 = Person(name="Aliya", age="20", city="Bishkek")
person_3 = Person(name="Nurayim", age="22", city="Bishkek")
person_4 = Person(name="Almaz", age="50", city="Bishkek")

print(person_1.introduse())
print(person_2.introduse())
print(person_3.introduse())
print(person_4.introduse())

print(person_1.is_adult())
print(person_3.is_adult())
print(person_3.is_adult())
print(person_4.is_adult())

print(person_1)
print(person_2)
print(person_3)
print(person_4)

