arr = list(map(int, input().split(" ")))

diff = min(arr)
rest = max(arr)
if diff > 0:   
    ans = 0
    ans += diff
    rest -= diff

    sec = rest//2
else:
    ans = 0
    sec  = rest//2
print(ans, sec)

