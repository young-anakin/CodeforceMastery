t = int(input())
for _ in range(t):
    n, r = list(map(int, input().split(" ")))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr)
    cp = 0
    rem = 0
    for ind in arr:
        cp += (ind//2)
        rem += ind %2
    ans = 0
    print(cp, rem)
    ans += r-cp
    print(ans)