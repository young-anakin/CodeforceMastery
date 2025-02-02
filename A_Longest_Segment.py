n, k = list(map(int, input().split(" ")))
ans = 1
arr = list(map(int, input().split(" ")))

cp = 1
for ind in range(1, n):
    if arr[ind] == arr[ind-1]:
        # print(ind, cp)
        ans = max(cp, ans)
        cp = 0
        cp +=1
    else:
        cp +=1

ans = max(cp, ans)

print(ans)