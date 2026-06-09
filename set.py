#set are mostly used in data science to store unduplicated values

s = {1 ,2 ,3 ,4 ,5}
#these are mutable, they cannot contain duplicates, it cannot be fetched through indexing and it is  semi-heterogenous , it can store string values 
# list = []
# tuple =()
# set = {} 


# set uses hash vlaues to store the data 

b = hash("hello")
print(b)

c = hash((1,2,4,5))

print(c)