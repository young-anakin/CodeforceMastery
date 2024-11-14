n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    arr.sort()
    # print(arr)

    if len(arr) == 2:
        print(arr[1] - arr[0]) 
    else:
        x = sz
        print(arr[x] - arr[x-1])