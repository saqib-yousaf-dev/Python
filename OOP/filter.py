
def even(x):
    if x%2 == 0:
        return True
    else:
        return False

numbers = [1,23,4,6,23,41,12,43]

result = filter(even , numbers)
#lambda function
result2 = filter(lambda x : True if x%2 ==0 else False , numbers)
print(list(result))
print(list(result2))