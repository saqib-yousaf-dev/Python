l = [ 4 , 5 , 15 , 13 , 19]

largest = l[0]
second = l[1]

for i in range(len(l)):
    if l[i] > largest:
     second = largest
     largest = l[i]
    elif i > second:
       second = i

print(largest , second)
