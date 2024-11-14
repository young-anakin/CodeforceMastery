n = int(input())
for ind in range(n):
    a,b,c  = list(map(int, input().split(" ")))

    cp = 0
    mn = min(a,b)
    mx = max(a,b)
    while mn < mx:
        mx -= c
        mn += c
        cp +=1
    print(cp)
