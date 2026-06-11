
from pathlib import Path
import os
def readpathandfile():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")



def createfile():
 
    readpathandfile()
    name = input("Enter File Name:- ")
    p = Path(name)
    if not p.exists():
        with open(p , "w") as fs:
            data = input("what your want to write here :- ")
            fs.write(data)
        ("FILE CREATED SUCCESSFULLLY")
    else:
        print("this file exists")
    

def readingfile():
    try:
        readpathandfile()
        name = input("Enter the file Name that you want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p , 'r') as f:
                print(f.read())
            print("File Readed Successfully")
        else:
            print("This is not a file")
    except Exception as err:
        print(f"Error in reading is: {err}")

def updatefile():
    readpathandfile()
    name = input("Enter the Name which you want to update:- ")
    p = Path(name)

    if p.exists() and p.is_file():
        print("press 1 for Changing the Name of file")
        print("Press for overwriting the data")
        print("Press 3 for Appending the data")
        res = int(input("Enter the Number:- "))

        if res == 1:
            name2 = input("Enter the New Name:- ")
            p2 = Path(name2)
            p.rename(p2)
        elif res == 2:
            with open(p , 'w') as fs:
                data = input("Enter the new Data:- ")
                fs.write(data)
        
        elif res == 3:
            with open(p , 'a') as fs:
                data = input("Enter the appending data:- ")
                fs.write(" "+data)

def deletefile():
    readpathandfile()
    name = input("Enter the filename which you want to del:- ")
    p = Path(name)

    if p.exists() and p.is_file():
        os.remove(name)
        print("file Removed successfully")
    else:
        print("No Such file Exists")



print("1. Create a File")
print("2. Read a File")
print("3. Update a File")
print("4. Deletion a file")

check = int(input("Enter the Number:- "))

if check == 1:
    createfile()
elif check == 2:
    readingfile()
elif check == 3:
    updatefile()
elif check ==4:
    deletefile()
