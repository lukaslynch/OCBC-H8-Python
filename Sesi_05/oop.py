#Define Class
class Dog:
    pass

#Define class with __init__
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Class has attribute
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

#instance as object
#Dog() #Will Error because param at __init__ require

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

#Call attribute at instance class
buddy.name
buddy.age
buddy.species

#Instance Method
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
#RUN Instance Method
miles = Dog("Miles", 4)
miles.description()
miles.speak("Woof Woof")
miles.speak("Bow Wow")

#Inheritance

#Dog Park Example
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

#Run Instance
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

#Run Class
buddy.speak("Yap")
jim.speak("Woof")

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

#inherit of child from parent
miles.species
buddy.name
print("#$$$$$$$$#")
print(jack)
print(jack.speak('GUK GUK'))
print("-------")
jim.speak("Woof")

#Extend the functionally of parent class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
    
miles = JackRussellTerrier("Miles", 4)
miles.speak()

miles.speak("Grrr")