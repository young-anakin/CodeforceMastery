arr1 = input()
arr2 = input()
fin = []
for a in range(len(arr1)):
    if arr1[a] == arr2[a]:
        fin.append('0')
    else:
        fin.append('1')
print("".join(fin))