n = int(input())
for ind in range(n):
    m, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.sort()
    fl = True
    arr1 = arr[0:m]
    arr2 = arr[m:]
    for ind in range(len(arr1)):
        if arr2[ind] - arr1[ind] < k:
            print("NO")
            fl = False
            break
    if fl == True:
        print("YES")

    