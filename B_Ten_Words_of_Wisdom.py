n = int(input())
for ind in range(n):
    sz = int(input())
    mx = 0
    ans = 0
    for j in range(sz):
        a, b = list(map(int, input().split()))

        if a <= 10:
            if b > mx:
                mx = max(mx, b)
                ans = j+1
    print(ans)