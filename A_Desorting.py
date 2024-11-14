n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    sorted_arr = sorted(arr)

    if sorted_arr != arr:
        print(0)
    else:
        minDistance = 1000000000000000000000
        for j in range(sz-1):
            minDistance = min(minDistance, arr[j+1] - arr[j])

        print((minDistance//2) + 1)
            