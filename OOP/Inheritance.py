#Four Pillars
#Inheritance
#Abstraction
#Polymorphism

class Factory: #parent Class
    a = "I am a attribute"
    def hello(self):
        print("Hello Bro")

class LahoreFactory(Factory): #child class
    pass


obj = Factory()
obj2 = LahoreFactory()
print(obj2.a)
print(obj.a)


class Animal:
    name1 = "animal"
    def __init__(self , name):
        self.name = name
    
    def show(self):
        print("hello your name is " , self.name)


class Human(Animal):
    name2 = "human"
    def __init__(self, name , age):
        super().__init__(name)
        self.age = age
    def show(self):
        print(f"You name is:- {self.name} and Age:- {self.age}")

class Robot(Human):
    name3 = "charlie"
    def __init__(self, name , age , functionality):
        super().__init__(name, age)
        

animal1 = Animal("Lion")
human2 = Human("Saqib" , 19)
human2.show()

robot1 = Robot("Bruh" , 2 , "safayi")
print(robot1.name1)
print(robot1.name2)
print(robot1.name3)

#multiple Inheritance

class Animal:
    name1 = "animal"
    def __init__(self , name):
        pass
    


class Human():
    name2 = "human"
    def __init__(self , name , age):
        pass
    
    def show(self):
        print(f"You name is:- {self.name} and Age:- {self.age}")

class Robot(Human , Robot):#when we will create the obj of robot now it willl require only first parent constructors parameters if we want all then we have to writ the ending one 
    name3 = "charlie"
    
obj = Robot("hehe" , 12)


#MultiLevel Inheritance

class Factory:
    def __init__(self , material , zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips , color):
        super().__init__(material, zips)
        self.color  = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color ):
        super().__init__(material, zips, color)
         