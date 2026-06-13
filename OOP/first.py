class Car:
    brand = "Toyota" #attribute

    #methods
    def hello(self ):
        print("how are you bruh... ")

    print("hello bro")

print(Car().brand)

#object

obj = Car()
obj.brand = "Suzuki"

print(obj.brand)

class Factory:
    #constructor runs automatically when the class is called and it can be used to generate the parameters

    def __init__(self , material , zips , pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print("Zips:" , self.zips)
        print("Material: " , self.material)
        print("Pockets: " , self.pockets)

  




livis = Factory("Jeans",3 ,2)  
Outfitters = Factory("Chinos", 1 , 4)

Outfitters.show()