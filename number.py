
inputNumber = int(input("Enter A Number:- "));
i = 1

while inputNumber > 0:
    print(f"Your {i} number is this: {inputNumber % 10}")
    inputNumber = inputNumber//10
    i = i+1 
