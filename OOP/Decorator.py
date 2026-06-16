#decorator is a function that modifies another funciton without actually changing its code

class Animal:
    @property
    def show(self):
        print("...")

obj = Animal()
obj.show

#fun is the hello function that will be a parameter bcz @decorate is written above on it
# 
def decorate(func):
    def wrapper(*args , **kwargs):
        print("Result")
        func(*args , *kwargs)
        print("I will print after the function")
    return wrapper


@decorate
def addition(a , b):
    print(a + b)

addition(12, 12)

#argument
def hehe(*args , **kwargs):
    total = 0
    for i in args:
        total += i

    print(total)

hehe(12, 12, 31, 15)

def information(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

information(a = 12, b = 23, x= 19)