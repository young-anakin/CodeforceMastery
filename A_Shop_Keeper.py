t = int(input())
import bisect, math
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    avg = math.ceil(sum(arr)/n)
    print(avg)
    # if avg in arr:
    #     print(avg)
    # else:
    #     x = bisect.bisect_left(arr, avg)
    #     print(arr[avg])