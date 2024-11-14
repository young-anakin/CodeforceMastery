n = int(input())

for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    mx = max(arr)
    mn = min(arr)
    print(mx - mn)