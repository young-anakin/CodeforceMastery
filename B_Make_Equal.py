n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    gives = 0
    takes = 0
    fl = True
    acc = sum(arr)//sz
    for ind in range(len(arr)):
        if arr[ind] >= acc:
            gives += arr[ind] - acc
        else:
            if acc - arr[ind] > gives:
                print("NO")
                fl = False
                break
            gives -= acc - arr[ind]
    if fl == True:
        print("YES")
