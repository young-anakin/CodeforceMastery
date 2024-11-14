t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(3):
        val = list(map(int, input().split(" ")))
        tmp = []
        for ind, j in enumerate(val):
            tmp.append((j, ind))
        arr.append(tmp)
    new = []
    for val in arr:
        val.sort(reverse = True)
        new.append(val[:3]) 
    arr = new
    mx = 0
        
    # print(new)
    for a, b in arr[0]:
        for c, d in arr[1]:
            if b == d:
                continue
            for e, f in arr[2]:
                if f == b or f == d:
                    continue
                mx = max(a+c +e, mx)
    print(mx)
