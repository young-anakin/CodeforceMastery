t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split(" ")))

    while len(str(a)) != 1:
        val = str(a)
        temp = 0
        for i in val:
            temp += int(i)
        val = str(temp)
        a = int(val)
    
    while len(str(b)) != 1:
        val = str(b)
        temp = 0
        for i in val:
            temp += int(i)
        val = str(temp)
        b = int(val)
    
    print(a, b)
