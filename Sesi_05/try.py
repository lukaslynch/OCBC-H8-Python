
#Parent Classes vs Child Classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

#Create new Class
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

#Try call class
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(type(miles) is Dog)
print(isinstance(miles, JackRussellTerrier))

class Mom:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color=hair_color

class Child(Mom):
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color