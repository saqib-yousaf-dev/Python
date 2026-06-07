
#range(Start , stop , step)
#default value of start is 0 and step is 1

for i in range(1, 10, 1):
    print(i) 

for c in range(12 , 2, -1):
    print(c)

t = int(input("Enter a number: "))
end = t*10 + 1
for i in range(t, end , t):
    print(i)

saqib = "Meta Ads Expert"
for i in range(len(saqib)):
    print(saqib[i]);

concat = ""
for i in range(len(saqib)-1, -1 , -1):
    print(saqib[i]);
    concat = concat + saqib[i]

print(concat)


#question new

