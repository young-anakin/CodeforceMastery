s, n = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

arr.sort()
mn = float("inf")
a = 0
b = s-1

while b <= len(arr)-1:
    mn = min(mn, arr[b] - arr[a])
    a +=1
    b +=1

print(mn)