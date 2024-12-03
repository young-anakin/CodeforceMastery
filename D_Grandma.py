t = int(input())
from collections import defaultdict, Counter
for _ in range(t):
    n = int(input())
    val = input()
    dd = Counter(val)
    ss = [key for key, ind in dd.items()]

    mx = float("inf")
    for ind in ss:
        l = 0
        r = n-1
        cp = 0
        fl = True
        while l < r:
            # print(l, r, val[r])
            if val[l] == val[r]:
                l +=1
                r -=1
            elif val[l] != val[r]:
                if val[l] == ind:
                    l +=1
                    cp +=1
                elif val[r] == ind:
                    r -=1
                    cp +=1
                else:
                    fl = False
                    break
        if fl:
            mx = min(mx, cp)
           
    if mx == float("inf"):
        print(-1)
    else:
        print(mx)          

    # print(ss)