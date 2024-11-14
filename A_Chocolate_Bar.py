t = int(input())
for _ in range(t):
    n, l, r, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.sort()
    cp = 0
    ans = 0
    curr = 0

    for ind in range(n):
        if arr[ind] >= l and arr[ind] <= r:
            curr += arr[ind]
            if curr <= k:
                cp +=1
        
        
    print(cp)

        