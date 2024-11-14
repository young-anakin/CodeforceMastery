n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    diff = 0
    prefix = 0
    new = []
    fl = True
    for j in range(sz):
        if arr[j] >= j:
            prefix += arr[j] - j
        else:
            if arr[j] + prefix < j:
                print("NO")
                fl = False
                break
            else:
                prefix -= (j - arr[j])
    if fl == True:
        print("YES")
