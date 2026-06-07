a = "ssfsfashfjkasds123%$23489##"


dig = 0
char = 0
spchar = 0
for i in a:
    if i.isdigit():
        dig = dig + 1
    elif i.isalpha():
        char = char + 1
    else:
        spchar = spchar + 1

print(f"Your Digits Are {dig}. Your Characters are {char} and Special Characters are {spchar}")