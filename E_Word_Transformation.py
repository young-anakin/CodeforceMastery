i = int(input())
from collections import Counter, defaultdict
for _ in range(i):
    indexes = defaultdict(int)
    # print(i)
    a, b = list(map(str, input().split(" ")))
    b = list(b)
    a = list(a)
    # a = a[::-1]
    # b = b[::-1]
    alist = Counter(a)
    blist = Counter(b)
    cp = 0
    fl = True
    if a == b:
        print("YES")
    else:
        while len(b) != 0:
            if b[-1] not in a:
                # print("NO")
                fl = False
                break
             
            if len(a) != 0:
                val = a.pop()
            
                if val == b[-1]:
                    # print(val)

                    b.pop()
                    blist[val] -=1
                
                elif blist[val] != 0:
                    # print(val)
                    # print("NO")
                    fl = False
                    break
            else:   
                print("NO")
                break
        
        if fl:
            print("YES")
        else:
            print("NO")
