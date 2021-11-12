# -*- coding: utf-8 -*-

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Dog2(Dog):
    def description(self):
        #return f"{self.name} is {self.age} years old"

         return super().description()


buddy = Dog2("Buddy", 9)
print(isinstance(buddy, Dog))


miles = Dog("Miles", 4)

# print(miles.name)
# print(miles.age)
# print(miles.species)
print(miles.description())
# print(miles.speak('Nomor wa nya berapa ya ?'))

miles2 = Dog2("Jack", 9)
print(miles2.description())
# buddy = Dog("Buddy", 9)

# print(buddy.name)
# print(buddy.age)
# print(buddy.species)


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# miles = Dog("Miles", 4)

# miles.description()

# miles.speak("Woof Woof")

# miles.speak("Bow Wow")


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")


# buddy.speak("Yap")
# jim.speak("Woof")


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# class JackRussellTerrier(Dog):
#     pass


# class Dachshund(Dog):
#     pass


# class Bulldog(Dog):
#     pass


# miles = JackRussellTerrier("Miles", 4)

# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)


# miles.species

# buddy.name

# print(jack)

# jim.speak("Woof")


# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"


# miles = JackRussellTerrier("Miles", 4)
# miles.speak()

# miles.speak("Grrr")
