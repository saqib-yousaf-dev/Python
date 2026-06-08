#in build data Structure: list , tuple , dictionary , set
#custome data structure: Stack , Queue, Linked List, Graph etc...

#list 
a = [12 , 16, 14, 15]

#mutable: it can be changed after creation
#Duplicates: 
# Ordered:
# Heterogeneous: 

print(a[0:2:1]);

#traversing 

for i in range(len(a)):
 print(a[i])

for i in a:
 print(i)

#help(list)
 #append

 l= [1,2,4,5,6]

 l.append(7)
 #l.insert(index to place , value)

 l.insert(5 , 0)
for i in l:
 print(i)
 
