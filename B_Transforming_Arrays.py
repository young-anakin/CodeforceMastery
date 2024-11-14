n = int(input())
for ind in range(n):
    sz = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    # print(a, b)
    from collections import defaultdict
    dd = defaultdict(int)
    fl = True
    for j in range(sz):
        if a[j] == b[j]:
            dd[a[j]] +=1
        elif b[j] > a[j]:
            if dd[1] == 0:
                fl = False
                break
            else:
                dd[a[j]] +=1
        else:
            if dd[-1] == 0:
                fl = False
                break
            else:
                dd[a[j]] +=1
    if fl == False:
        print("NO")
    else:
        print("YES")