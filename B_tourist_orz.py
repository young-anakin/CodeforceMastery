t = int(input()) 
for _ in range(t):
    n, z = map(int, input().split()) 
    a = list(map(int, input().split()))  
    
    max_val = max(a)  
    
    
    for i in range(n):
        while (a[i] | z) > a[i]:
            a[i] |= z
    
    for i in range(n):
        if (a[i] & z) != 0:
            a[i] |= z
    
    max_val = max(max_val, max(a))
    print(max_val)
