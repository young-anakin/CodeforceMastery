t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    even = []
    mn = 0
    odd = 0
    maxofevens = 0

    for ind in arr:
        if ind %2 == 1:
            mn = max(mn, ind)
            odd +=1
        else:
            maxofevens = max(maxofevens, ind)
            even.append(ind)
    even.sort()


    # print(maxofevens)
    if odd == 0 or n-odd == 0:
        print(0)
    else:
        # print(even)
        cp = 0
        for ind in even:
            if ind %2 == 1:
                continue
            else:
                if ind < mn:
                    cp +=1
                    mn = max(mn, ind + mn)
                else:
                    mn = maxofevens + mn
                    cp +=2
            # print(mn)
        print(cp)