
d = {}
#if these braces are empty then it will not considered as set it will be dictionary
print(type(d))

#dictionary basically are like objects
#they have key and value pairs bro
#mutable but key can't changed but values can changed
#duplicate value can exist
#order: it follows the insertion order and key will be used for indexing
#Heterogenous Nature: it can store any keys and values integers string floats and even other dictionaries


d = {1 : "hello",
     2: 56

     }

a = {
    10: 1000,
    20: 2000,
    30: 3000,
    40: 4000
}

print(a[10])

#We can Use CRUD Operaitons

a[10] = 100

a.update({50:500})
print(a)
#instead a[50] = 500

del a[30]
print(a)


for i in a:#a.values() it will be easy to directly access the values
     print(i)#it will print keyss
     print(a[i])


#dictionary methods
#help(dict)

#a.clear()

#deep copy and shallow copy

a = [1 ,2 , 3, 4, 20]
b = a

b[0] = 15
print(a)
#it is deep copy it will change the value from a also

#shallow copy will just copy and then it wil not effect the other

a2 = a.copy()



print(d.items)

#questions

#merging two dictionaries
d1 = { 10:200 , 20: 400}
d2 = {40 : 100 , 50: 100}

for i in d2:
     d1[i] = d2[i]
print(d1)

#frequency counting in list

a = [1,2,3,4,5,1,1,1,2,2,2,2]
result = {}
for i in a:
    if i in result.keys():
      result[i] +=1
    else:
     result[i] = 1

print(result)

#combining two dictionaries
d1 = {10:200 , 20: 400 , 30:100}
d2 = {30: 300, 40 : 100 , 50: 100}

for i in d2:
   if i in d1:
    d1[i] = d1[i] + d2[i]
   else:
      d1[i] = d2[i]

print(d1)