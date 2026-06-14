#Encapsulation meas putting data and code function togethe rin one place.

class Factory:
    a = "pune"

    def show(self):
        print("hello i'm a fcatory")
    
obj = Factory()

obj.a = "Bhopal" #now it is changed but we want unchange in encapsulation 

#we can make the attributes by adding single underscore _a

class Car:
    __name = "Nothing" # private
    _color = "" #protected
    #we can also make the methods privat by adding __ double underscore like this:
    # def __show

    def show(self):
        print(Car.__name)

obj = Car()

obj.show()