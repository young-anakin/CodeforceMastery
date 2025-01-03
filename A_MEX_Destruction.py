t = int(input())
for _ in range(t):
    cp = 0
    n = int(input())
    arr = list(map(int, input().split(" ")))

    if len(arr) == arr.count(0):
        print(0)
    elif arr.count(0) == 0:
        print(1)
    elif arr.count(0) == 1:
        if arr[0] == 0 or arr[-1] == 0:
            print(1)
        else:
            print(2)
    elif arr.count(0) >= 2:
        if arr[0] == 0 or arr[-1] == 0:
            print(2)
        elif arr[0] == 0 and arr[-1] == 0:
            print(1)
    else:
        print(2)

