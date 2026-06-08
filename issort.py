a = [12, 13, 14, 15, 16]

sorted_list = True

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("sorted")
else:
    print("not sorted")