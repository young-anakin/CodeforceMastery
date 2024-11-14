r, c = list(map(int, input().split(" ")))
arr = []
for ind in range(r):
    for j in range(c):
        arr.append((ind+1, j+1))

fl = True
first = 1
print(arr)
new = []
while arr:
    for val in arr:
        print(val, first)
        if first in val:
            new.append(first)
    if len(arr) == 0:
        break
    first +=1
    fl = not(fl)
    break
print(arr)
if fl:
    print("Akshat")
else:
    print("Malvika")