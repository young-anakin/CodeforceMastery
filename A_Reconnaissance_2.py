n = int(input())
arr = list(map(int, input().split(" ")))
arr.append(arr[0])
a, b = 0, 0
mn = float("inf")
for ind in range(n):
    if abs(arr[ind] - arr[ind+1]) < mn:
        # if ind+1 
        if ind+2 > n:
            a, b = ind+1, 1
        else:
            a, b = ind+1, ind+2
        mn = abs(arr[ind] - arr[ind+1])

print(a,b)