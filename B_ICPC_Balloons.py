n = int(input())
for ind in range(n):
    x = int(input())
    val = input()
    from collections import defaultdict
    dd = defaultdict(int)
    ans = 0
    for ind in range(x):
        if dd[val[ind]] == 0:
            ans +=2
            dd[val[ind]] +=1
        else:
            ans +=1
    print(ans)