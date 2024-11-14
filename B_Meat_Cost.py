t = int(input())
init = [0, 1000]
ind = 0
mn = init[1]
ans = 0
for ind in range(t):
    meat, price = list(map(int, input().split(" ")))
    mn = min(price, mn)
    ans += (meat * mn)
print(ans)
