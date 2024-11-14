t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    front = 0
    ans = 0
    fl = True
    while arr:
        val = arr.pop()
        if val > front:
            if fl:
                ans = max(ans, val)
                print(ans)
            else:
                ans +=1
        else:
            ans +=1
            fl = False
        front = val
    print(ans)