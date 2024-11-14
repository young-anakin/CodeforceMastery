a, b = list(map(int, input().split(" ")))
mn = min(a,b)
ans = 1
for ind in range(1, mn+1):
    ans *= ind

print(ans)