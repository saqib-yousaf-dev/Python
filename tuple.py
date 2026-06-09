
# tuple creation

a = (1 , 2, 3, 4 ,5 )
print(type(a))

#immutable , duplicate values can exist , Ordered and it can be accessed through Indexing , it also have heterogenous feature

b  = ( 1 ,2 , 5 ,6 , 5.5 , print() , "hello")

for i in b:
    print(i);


index = a.index(5)
print(index)

print(a.count(5))

#tuple unpacking
one, two ,three , four = (1 , 2 ,3 , 4)

 