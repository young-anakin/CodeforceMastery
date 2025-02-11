import bisect

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    cur = -1 * float("inf")
    possible = True
    
    for i in range(n):
        best = float("inf")
        
        if a[i] >= cur:
            best = a[i]
        
        required = cur + a[i]
        pos = bisect.bisect_left(b, required)
        if pos < len(b):
            candidate = b[pos] - a[i]
            best = min(best, candidate)
        
        if best == float("inf"):
            possible = False
            break
        
        cur = best
    
    if possible:
        print("YES")
    else:
        print("NO")
