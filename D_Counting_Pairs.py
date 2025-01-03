from bisect import bisect_right, bisect_left

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    sm = sum(arr)
    arr.sort()
    res = 0
    for i in range(n):
        cur = sm - arr[i]
        if cur < x:
            continue
        val1 = cur - x
        val2 = cur - y
        l = bisect_left(arr, val2, i + 1)
        r = bisect_right(arr, val1, i + 1) - 1
        # print(l, r)
        # if r < l:
        #     continue
        # if i >= l and i <= r:
        #     res -= 1
        res += r - l + 1
    print(res)
