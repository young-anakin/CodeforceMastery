t = int(input())
from collections import defaultdict, Counter
import bisect
z = 1
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    dd = defaultdict(int)
    tot = defaultdict(list)
    arr = list(map(str, input().split(" ")))
    val = set()
    # val.add(1)
    ans = [set() for i in range(n+1)]
    # print(ans)
    for ind in range(1, n+1):
        tot[arr[ind-1]].append(ind-1)
        dd[arr[ind-1][0]] +=1
        dd[arr[ind-1][1]] +=1
        val = set([arr[ind-1][0], arr[ind-1][1]])
        # print(val)
        tmp = ans[ind-1]
        tmp.update(val)
        ans[ind].update(tmp)
    
    ans.pop()
    # print(arr)
    # print(tot)
    # print(ans)
# 
    all = ["BG", "BR", "BY", "GR", "GY","RY" ]
    for _ in range(m):
        a, b = list(map(int, input().split(" ")))
        
        cp = Counter(arr)
        # print(z, a, b)
        z+=1
        if a == b:
            # print("a")
            print(0)
            continue
        elif len(cp) == 2:
            # print('b')

            if arr[a-1][0] == arr[b-1][0] or arr[a-1][0] == arr[b-1][1] or arr[a-1][1] == arr[b-1][0] or arr[a-1][1] == arr[b-1][1]:
                # print("champion")
                print(abs(a-b))
                continue
            else:
                print(-1)
                continue
            # tt = set(arr)
            # tt = list(tt)
            # if tt[0][0] != tt[1][0] and tt[0][0] != tt[1][1] and tt[0][1] != tt[1][0] and tt[0][1] != tt[1][1]: 
            #     print(tt[0], tt[1])
            #     print(-1)
            #     continue
                
        # else:
        # print('c')
        mn = min(a,b)-1
        mx = max(a,b)-1
        tmp = arr[mx]
        if tmp[0] in ans[mx-1] or tmp[1] in ans[mx-1]:
            print(mx-mn)
        else:
            ss = float("inf")
            for ind in all:
                # print(tot[ind])
                if ind != arr[mx] and ind in tot:
                    x = bisect.bisect_right(tot[ind], mx)
                    if x < len(tot[ind]) and tot[ind][x] > mx:
                        ss = min(ss, tot[ind][x])
            print(abs(ss-mx) + abs(ss-mn))
    