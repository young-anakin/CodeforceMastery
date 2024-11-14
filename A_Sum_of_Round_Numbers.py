t = int(input())
for _ in range(t):
    val = input()
    n = len(val)-1
    ans = []
    for ind in range(len(val)):
        tmp = int(val[ind])* (10**n)
        if tmp != 0:
            ans.append(tmp)
        n-=1
    print(len(ans))
    print(*ans)