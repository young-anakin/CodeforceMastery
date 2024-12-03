t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    ss = sorted(arr)
    # print(ss)
    if arr == ss:
        print(0)
    else:
        mn, mx = min(arr), max(arr)

        if arr[0] == mn or arr[-1] == mx:
            print(1)
        # 5 4 3 2 1
        # 2 3 4 5 1
        # 2 1 3 4 5
        # 1 2 3 4 5
        elif arr[0] == mx and arr[-1] == mn:
            print(3)
        # 5 1 2 3 4
        # 1 2 3 5 4
        # 1 2 3 4 5
        elif arr[0] == mx or arr[-1] == mn:
            print(2)
        else:
            print(2)