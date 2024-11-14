t = int(input())
from collections import Counter
for _ in range(t):
    n, m , k = list(map(int, input().split(" ")))

    tmp = []
    for ind in range(m):
        tmp .append(str(ind)) 
    new = tmp
    while len(new) <= n:
        new += tmp
    

    new = new [0:n]
    cp = Counter(new)
    if len(cp) != 1:
        mx, val = 0, 0
        for key, values in cp.items():
            if values > mx:
                mx = values
                val = key
        i = 0
        for ind in range(len(new)):
            if new[ind] != val:
                i +=1
            if i == k:
                break
        # print(new)
        # print(cp)
        if cp[val] + i == n:
            print("NO")
        else:
            print("YES")


    else:
        print("NO")
    
