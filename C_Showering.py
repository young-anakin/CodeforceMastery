t = int(input())
for _ in range(t):
    n,s,m = list(map(int, input().split(" ")))
    cp = 0
    last = 0
    fl = True
    for _ in range(n):
        a, b = list(map(int, input().split(" ")))
        if abs(last - a) >= s:
            fl = False
        else:
            last = b
    
    if (m - last) >= s:
        fl = False
    if fl:

        print("NO")
    else:
        print("YES")