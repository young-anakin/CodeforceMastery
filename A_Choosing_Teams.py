n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

cp = 0
arr.sort()
ovans = 0
for ind in range(n):
    if arr[ind] + k <= 5:
        cp +=1
    if cp == 3:
        cp = 0
        ovans +=1

print(ovans)