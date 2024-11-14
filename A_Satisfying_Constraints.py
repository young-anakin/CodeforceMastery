from collections import defaultdict
n = int(input())
for ind in range(n):
    sz = int(input())
    wrong = []
    s = 0
    l = 1000000000
    for j in range(sz):
        x, y = list(map(int, input().split(" ")))
        if x == 1:
            s = max(s, y)
        elif x == 2:
            l = min(l, y)
        else:
            wrong.append(y)
    # print(s, l)
    ans = l -s 
    if l -s > 0:
        for j in range(len(wrong)):
            if s <= wrong[j] and l >= wrong[j]:
                ans -=1
        print(ans+1)
    else:
        print(0)
