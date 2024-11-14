from collections import defaultdict

for _ in range(int(input())):
    sz = int(input())
    li = list(map(int, input().split()))
    
    dd = defaultdict(int)
    for num in sorted(li):
        dd[num] += 1
    new = set()    
    old = 0
    sub = set()

    
    while dd[old] >= 2:
        sub.add(old)
        new.add(old)
        old += 1
    
    if dd[old] > 0:
        print(-1)
        continue
        
    final = 0
    
    for i in range(sz):
        if li[i] in sub:
            sub.remove(li[i])
        if len(sub) == 0:
            final = i + 1
            break
    
    for i in range(final, sz):
        if li[i] in new:
            new.remove(li[i])
    
    if len(new):
        print(-1)
    else:   
        print(2)
        print(1, final)
        print(final + 1, sz)