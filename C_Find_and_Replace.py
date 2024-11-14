from collections import defaultdict
n = int(input())
for ind in range(n):
    sz = int(input())
    
    dd = defaultdict(int)
    val = input()
    dd[val[0]] = 7
    fl = True
    for j in range(1, sz):
        if dd[val[j]] == 0:

            if dd[val[j-1]] == 7:
                dd[val[j]] = 8
            else:
                dd[val[j]] = 7
        elif dd[val[j]] == 7:
            if dd[val[j-1]] == 7:
                fl = False
                break
        elif dd[val[j]] == 8:
            if dd[val[j-1]] == 8:
                fl = False
                break
    if fl == False:
        print("NO")
    else:
        print("YES")

