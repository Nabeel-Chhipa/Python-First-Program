class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
personOne = Person('Nabeel', 27)
personTwo = Person('Usama', 28)
print(personOne.getName())