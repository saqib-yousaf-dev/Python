#special methods that start with double underscore like def __init_(self, nane)

class Animal():
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return (f"Your name is {self.name}")
    def __add__(self, other):
        return (f"your sum of ages are: {self.age + other.age}")

obj = Animal("Lion" , 14)
obj2 = Animal("Dolphin", 14)
obj3 = Animal("Tiger" , 15)
print(obj + obj2)
print(obj + (obj2,obj3))