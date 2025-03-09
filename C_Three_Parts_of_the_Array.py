t = int(input())
arr = list(map(int, input().split(" ")))
ps = [0]
import bisect
for ind in arr:
    ps.append(ps[-1] + ind)



mx = 0
# (ps)
for i in range(1, len(arr)):
    val = ps[i]
    rem = ps[-1] - val # 5

    check = bisect.bisect_left(ps, rem, 0, i)

    if check < t and ps[check] == rem:
        mx = max(mx, rem)
print(mx)