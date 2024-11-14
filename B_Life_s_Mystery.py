arr = input()

# Stack solution
new = []
i = len(arr)-1
while i >= 0:
    if  len(new) != 0:
        if arr[i] == new[-1]:
            new.pop()
            i -=1
            continue
    if i == 0:
        new.append(arr[i])
        i -=1
        continue
    if arr[i] == arr[i-1]:
        
        i -=2
    else:
        new.append(arr[i])
        i -=1
    # print(i)
print("".join(new[::-1]))
# for ind in range(1, len(arr)):
#     if arr[-ind] == arr[-ind+1]:
#         continue
#     else:
#         new.append(arr[-ind])

# print("".join(new))