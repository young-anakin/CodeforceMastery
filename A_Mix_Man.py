t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))
    
    for ind in range(n):
        if arr1[ind] > arr2[ind]:
            arr1[ind], arr2[ind] = arr2[ind], arr1[ind]
    
    # print(arr1, arr2)
    print(max(arr1) * max(arr2))