#method overriding 

class Animal:
    def show(self):
        print("hello")
class Human(Animal):
    def show(self):
        print("hello bro")

obj = Human()
obj.show()

#it will compile the Human Show function because human show function overrides it

#method Overloading does not exist bro means we can create multiple functin same name but different parameters

#Duck Typing
#Python follows tthat if it walks like a duck and quacks like a duck. it must be a duck

#Duck typing means basically like above if we creat two indivdual objects of Animal and Human then you know it will be easy