t = int(input())

for _ in range(t):
    val = list(input())
    x= len(val)
    
    for i in range(x):
        mx = int(val[i])
        pos = i
        
        for fl in range(i, x):
            if fl - i > 9:
                break
            
            cp = int(val[fl]) - (fl - i)
            if cp > mx and cp >= 0:
                mx = cp
                pos = fl
        
        if pos != i:
            val.pop(pos)
            val.insert(i, str(mx))
    
    print("".join(val))
