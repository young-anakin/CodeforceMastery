t = int(input())

for _ in range(t):
    res = 0
    sz, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    for i in range(30, -1, -1):
        zero = 0
        curr = 1 << i
        for x in arr:
            if x & curr == 0:
                zero +=1
            

        if zero <= k:
            k -= zero
            res |= (1 << i)
        
    print(res)