#it does not exist in python but it can use by library

#Abstration wil be used when you want some 

#library
from abc import ABC, abstractmethod


class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self , side):
        self.side = side

    def perimeter(self):
        print("Paramete of square:- 4")
    def area(self):
        print("Area of Square:- 19")
    
class Circle(abstract):
    def __init__(self , radius):
        self.radius = radius
    
obj = Square(8)
#now it will require the perimeter and area bro