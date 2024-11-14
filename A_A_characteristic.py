t = int(input())
from collections import defaultdict
i = 0
for _ in range(t):
    a = defaultdict(int)
    b = defaultdict(int)
    # print(i)
    # i +=1
    n, k = list(map(int, input().split(" ")))
    ones = []
    for ind in range(1, 101):
        a[((ind * (ind-1))//2)] = ind
        ones.append(((ind * (ind-1))//2))
    fl = True
    # print(ones)
    # print (a)
    if k in ones:
        t = [1 for _ in range(a[k])]
        # for _ in range(n-a[k]):
        #     t.append(-1)
        # print(t)
        if len(t) == n:
            print("YES")
            print(*t)
            continue
    
    for x in ones:
        for z in ones:
            if x + z == k and a[x] + a[z] == n:
                print("YES")
                fl = False
                o = [1 for _ in range(a[x])]
                z = [-1 for _ in range(a[z])]
                z.extend(o)
                print(*z)
            elif x + z > k:
                break
        if not fl:
            break

    if  fl:
        print("NO")
    



#     if fl:
#         print(0)
    
# print(a)