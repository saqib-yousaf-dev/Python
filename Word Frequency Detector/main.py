import pathlib as Path
import os 

#Word Frequency Detector 

h = open("hello.txt" , 'w')
h.write("mera naam saqib hai mai 19 saal ka hun and my dream is to become a best developer and get hired by a multi national software houses")
h.close()

with open("hello.txt" , 'r') as fs:
    data = fs.read()

alphabets = 0
digits = 0
spchar  = 0
for i in data:
    if i.isalpha():
        alphabets = alphabets + 1
    elif i.isdigit():
        digits = digits + 1
    else:
        spchar = spchar + 1

print("Characters: " , alphabets)
print("Digits: " , digits)
print("Special Characters: " , spchar)

# 1. Read the file data just like before
with open("hello.txt" , 'r') as fs:
    data = fs.read()

# 2. Split the paragraph into a list of individual words
words = data.split() 
print("List of words:", words)
print("Total word count:", len(words))