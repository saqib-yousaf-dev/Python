# File Handling - CRUD Operations

# 1. READ (Make sure this directory and file actually exist on your PC!)
try:
    p = open(r"C:\read\AiOLog.txt", 'r')
    print(p.read())
    p.close()
except Exception as err:
    print(f"The system cannot find the path specified for AiOLog.txt, skipping... {err}")

print("\n--- Writing to File ---")

# 2. WRITE (Creates or overwrites 'aalu.txt')
r = open("aalu.txt", 'w')
r.write("Hello My name is Saqib Yousaf and i want to become a best developer.\n")
r.close()

# 3. READ 'aalu.txt' (Changed variable name from 'open' to 'file_reader')
file_reader = open("aalu.txt", 'r')
print(file_reader.read())
file_reader.close()

print("--- Appending to File ---")

# 4. APPEND (Changed variable name here too)
file_append = open("aalu.txt", 'a')
file_append.write("And my age is 19 years old.")
file_append.close()

# Final Read to see the appended result
file_reader = open("aalu.txt", 'r')
print(file_reader.read())
file_reader.close()