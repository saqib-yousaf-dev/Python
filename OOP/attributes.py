#class attribute
#instance attrubute

class Animal:
    name = "lion"   #class Attribute

    def __init__(self , age):
        self.age = age #instance attribute
    
    def show(self):#instance method
        print(self.age)
    #self will locate the object position 
    #cls will locate or point the class position
    #Class methods
    @classmethod
    def hello(cls):
        print("Hello Brother")

    # Static method
    @staticmethod
    def static():
        print("how are you bro")

obj = Animal(12)
obj.show()

obj.hello() # but we can't here access the self values of variables and other
#cls will point to class position

obj.static()