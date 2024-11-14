n = int(input())
arr = []
for ind in range(n):
    x = list(map(int, input().split(" ")))
    arr.append(x)
cp = 0
for ind in range(len(arr)):
    for j in range(len(arr)):
        if ind == j:
            continue
        if arr[ind][0] == arr[j][1]:
            cp +=1

print(cp)
