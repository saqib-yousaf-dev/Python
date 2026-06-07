a = 12
print(type(a))

#imganiry datatype
a = 14j

print(type(a))

#THere are not any characters

a = True
b  = False

print(type(a))  

#indexing will be in storing the data in the list and tuple and strings
a = "Saqib Yousaf"

#start,end,steps 

c = a[0:3:1]
print(c)

c = a[6:12:1]
print(c);

#type conversion str(),int(),float(),complex() 


c =  int(input("What is your age: "))
print(type(c));

#Flow Division: it will automatically convert the float result into integer it will remove the decimal part and give you the integer part only
print(c//2)


money = 12

if 10 < money < 20:
    print("You can buy the Choco Bar")

elif 20 < money < 30:
    print("You can buy the Mango Dolly Ice Cream")
else:    
    print("You cannot buy the item")
