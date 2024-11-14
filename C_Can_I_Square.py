t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    sm = sum(arr)
    # print(sm)
    low = 0
    high = sm
    fl = False
    while low <= high:
        mid = (low + high)//2
        if mid * mid > sm:
            high = mid-1
        elif mid * mid == sm:
            fl = True
            break
        else:
            low = mid+1
    if fl:
        print("YES")
    else:
        print("NO")