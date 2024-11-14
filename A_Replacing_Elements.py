n = int(input())
for ind in range(n):
    sz, tar = list(map(int, input().split(" ")))

    arr = list(map(int, input().split(" ")))

    arr.sort()
    # print(arr)
    if arr[-1] <= tar:
        print("YES")
    elif arr[0] > tar or arr[1] > tar:
        print("NO")
    elif arr[0] + arr[1] > tar:
        print("NO")
    else:
        print("YES")