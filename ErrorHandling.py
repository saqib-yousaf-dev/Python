a = 5
#three errors: indentation , syntax and tab error can be solved using erorr handling
# all other errors are exceptions


try:
    print(10/a)

except ZeroDivisionError:
#for all error catching
#except Exception as err:
    print("Sorry you cannot divide it by zero")
    #print(f"sorry the error is this {err}")

except Exception as err:
    print(f"error is:- {err}")

else:#it will be written if there is not any exception bruh...
    print("good there is no exception")\
    
finally: #it will run no matter what
    print("I will run no matter what happen bruhhh")

age = int(input("Enter your age:- "))
if age<10 or age>18:
    raise ValueError("Your Age must be above than 1 18 due to Bise Multan")
else:
    print("welcome Home")
