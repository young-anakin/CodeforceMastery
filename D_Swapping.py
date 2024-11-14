t = int(input())
for _ in range(t):
    n, k, m = list(map(int, input().split(" ")))
    tot = 0
    fl = True
    mn, mx = 0, 0
    # print(1)
    for _ in range(m):
        a, b = list(map(int, input().split(" ")))
        if fl:
            if a <= k <= b:
                tot += abs(b-a)
                mn, mx = min(a,b), max(b,a)
                fl = False
        else:
            if a > mx:
                continue
            elif b < mn:
                continue
            elif a <= mn and b >= mx:
                mn = min(mn, a)
                mx = max(mx, b)
            elif a <= mn and b <= mx:
                mn = min(mn, a)
                mx = max(mx, b)
                # print("changed", mn, a)
            elif b >= mx and a <= mx:
                mn = min(mn, a)
                mx = max(mx, b) 
            elif mn <= a <= b <= mx:
                mn = min(mn, a)
                mx = max(mx, b)
            else:
                continue
        # print(mn, mx)
    print(abs(mx - mn) + 1)
            
