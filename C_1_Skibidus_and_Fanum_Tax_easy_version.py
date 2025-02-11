t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    B = int(input())
    
    if n == 1:
        print("YES")
        continue
    
    dp0, dp1 = True, True
    cur0, cur1 = a[0], B - a[0]
    for i in range(1, n):
        candidate0 = a[i]
        candidate1 = B - a[i]
        
        new0, new1 = False, False
        
        if dp0 and cur0 <= candidate0:
            new0 = True
        if dp1 and cur1 <= candidate0:
            new0 = True
        
        if dp0 and cur0 <= candidate1:
            new1 = True
        if dp1 and cur1 <= candidate1:
            new1 = True
        
        dp0, dp1 = new0, new1
        cur0, cur1 = candidate0, candidate1
    
    if dp0 or dp1:
        print("YES")
    else:
        print("NO")
    
    print("------------")
