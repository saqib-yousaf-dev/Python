a = 12
#ternary operation
print("even") if a%2 == 0 else print("odd")


# list comprehension
l = [i for i in range(1,21) if i % 2 == 0]

print(l)

#dictionary comprehension
l = {i : i**2 for i in range(1,21) if i % 2 == 0}

#lambda Function

product = lambda a, b : a*b

print(product(13,12))

number = lambda c : "even" if c%2 == 0 else "odd"