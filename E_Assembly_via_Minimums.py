t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    tt = set(arr)
    ab = list(tt)
    mx = max(ab)
    ab.sort(reverse=True)
    # print(ab)
    cp = Counter(arr)
    # print(cp)
    ans = []
    alls = 0
    for ind in ab:
        if cp[ind] == 1:
            ans.append(ind)
            ans.append(ind)
            alls +=2
        else:
            if cp[ind] == alls:
                ans.append(ind)
                alls +=1
            else:
                cp[ind] -=alls
                ans.append(ind)
                alls +=1
                while cp[ind] != 0:
                    ans.append(ind)
                    cp[ind] -=alls
                    alls +=1

    # print(cp)
    print(*ans)

