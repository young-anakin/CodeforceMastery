n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort(reverse=True)
    sm = 0
    j = 0
    while j < len(arr):
        sm += min(arr[j], arr[j+1])
        j+=2
    print(sm)