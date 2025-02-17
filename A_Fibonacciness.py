t = int(input())
for _ in range(t):
    a, b, d, e = list(map(int, input().split(" ")))
    c = a+b
    cp = 0

    if a + b == c:
        cp +=1
    if b+c == d:
        cp +=1
    
    if c+d == e:
        cp +=1
    
    cp2 = 0

    c = e-d

    if a+b == c:
        cp2 +=1
    if b+c == d:
        cp2 +=1
    if c+d == e:
        cp2 +=1
    
    print(max(cp, cp2))
