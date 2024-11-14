n = int(input())
for ind in range(n):
    m, k = list(map(int, input().split(" ")))
    val = input()
    ans = ""
    fl = False
    for j in range(m):
        if int(val[j]) < k:
            ans += val[0:j] + str(k) + val[j:]
            fl = True
            break
    if fl == False:
        ans = val + str(k)
    print(ans)           