k = int(input())
arr = list(map(int, input().split(" ")))
arr.sort(reverse=True)
# print(arr)
cp = 0
if k == 0:
    print(0)
else:
    fl = True
    for ind in range(12):
        cp += arr[ind]
        if cp >= k:
            fl = False
            print(ind+1)
            break
    if (fl):
        print(-1)