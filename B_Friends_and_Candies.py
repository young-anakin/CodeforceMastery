t = int(input())
import bisect
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    # print(arr)

    md = sum(arr)/n
    if int(md) != md:
        print(-1)
    # elif len(arr) == 1 or md == 1:
    #     print(0)
    else:
        x = bisect.bisect_right(arr, md)
        print(n-x)