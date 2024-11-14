t = int(input())
from bisect import bisect_right

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    arr.sort()
    # print(arr)
    total = set(arr)
    mx = 0
    tt = len(total)
    for val in total:
        x = bisect_right(arr, val)
        y = bisect_right(arr, (val-1))
        # print(y, x)
        affordable = abs(x-y)
        remaining = tt - 1
        # print(affordable, remaining)
        if affordable > remaining:
            if remaining + 1 == affordable:
                mx = max(mx, remaining)
            else:
                mx = max(mx, remaining+1)
            # if (remaining + affordable) % 2 == 0:
            #     mx = max(mx, min(affordable, tt))
            # else:
            #     mx = max(mx, min(affordable, remaining))
        else:
            mx = max(mx, min((abs(x - y), n - (abs(x-y)))))
    print(mx)