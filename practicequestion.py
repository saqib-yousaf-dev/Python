a = 567;
string = ""
while a > 0:
     b = a%10
     a = a//10
     string = string + str(b);

end = int(string)
print(end)
print(type(end))