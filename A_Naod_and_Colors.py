    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split(" ")))
        ans = 0
        mx = 0
        for ind in range(n-1):
            if arr[ind] == arr[ind+1]:
                ans +=1
                mx = max(ans, mx)
            else:
                mx = max(ans, mx)
                ans = 0
        print(mx+1)