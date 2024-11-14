t = int(input())
al = "abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    ans = ""
    for i in range(n):
        if i % k == 0:
            cp = 0
        ans += al[cp]
        cp +=1
    print(ans)
    