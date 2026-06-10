#set are mostly used in data science to store unduplicated values

s = {1 ,2 ,3 ,4 ,5}
#these are mutable, they cannot contain duplicates, it cannot be fetched through indexing and it is  semi-heterogenous , it can store string values 
# list = []
# tuple =()
# set = {} 


# set uses hash vlaues to store the data 

b = hash("hello")
print(b)

c = hash((1,2,4,5))

print(c)

#Set Traversing

for i in s:
    print(i)

hehe = {1 , 4 ,5 , 16 , 8 , 9 , "Hello", 18}

for i in hehe:
    print(i)
    
     
#set methods provide the mutability
# add , remove , discard , pop(it will remove the smaller hash value from the set)
#clear will remove all the elements

s.remove(4)
s.pop()
for i in s:
    print(i)


e = {1 , 2 ,3 ,4 ,5}
f = {4 ,5 ,6 ,7 ,8}

result = e.union(f) # e|f we can also write this
result_inter = e.intersection(f)
result_diff = e.difference(f)

#symmetric diff A = 1, 2 ,3 and B = 3 ,4 ,5 then r = 1 ,2 ,4 ,5
result_symm = e^f

e -= f
print(result)
print(result_inter)
print(result_diff)
print(result_symm)

