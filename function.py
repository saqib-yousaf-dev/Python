
def hello(a , b = 30):
    print("Hello World ")
    print(a+b)

hello(40)


def pallendome(str):
            #range(length(start , stop , step)
    txt = ""
    for i in range(len(str)-1 , -1 , -1):
        txt = txt + str[i]
    
    if str == txt: 
        return True

    else:
        print("NOt Pallindrome")


pallendome("Hello")
ispallendome = pallendome("NAMAN")
if ispallendome == True:
    print("It is Pallendome Text")