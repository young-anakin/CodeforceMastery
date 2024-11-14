n = int(input())
for ind in range(n):
    size = int(input())
    ans = 0
    val = input()
    for ind in range(size):
        ans = max(ans, ord(val[ind])-96)
    print(ans)
