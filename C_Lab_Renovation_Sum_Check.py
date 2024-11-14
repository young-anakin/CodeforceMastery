t = int(input())
arr = []
for _ in range(t):
    sub = list(map(int, input().split(" ")))
    arr.append(sub)


transpose = [[] for _ in range(t)]
# print(transpose)

for ind in range(t):
    for j in range(t):
        transpose[j].append(arr[ind][j])


# print(transpose)
# print(arr)
fl = True
for ind in range(len(arr)):
    for j in range(len(arr)):
        if arr[ind][j] != 1:
            # print("sub", arr[ind][j], transpose[ind])
            tmp = True
            for z, val in enumerate(arr[ind]):
                if z != j:
                    # print(arr[ind][j], val, arr[ind][j] - val)
                    if arr[ind][j] - val in transpose[j]:
                        tmp = False
                        break
            # print(tmp)
            if tmp:
                fl = False
                break
    if not fl:
        break
            

if fl:
    print("Yes")
else:
    print("No")