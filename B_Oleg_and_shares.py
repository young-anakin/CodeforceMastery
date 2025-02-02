n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
mn = min(arr)
fl = True
cp = 0
for ind in arr:
    if abs(ind - mn) % k == 0:
        cp += abs(ind-mn)//k
    else:
        fl = False
        break

if fl:
    print(cp)
else:
    print(-1)