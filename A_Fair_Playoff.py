n = int(input())
for ind in range(n):
    first = [0,2]
    second = [3,4]
    arr = list(map(int, input().split(" ")))
    new_arr = sorted(arr)
    max1 = new_arr[3]
    max2 = new_arr[2]
    arr1 = sorted([max1, max2])
    arr2 = sorted([max(arr[0], arr[1]), max(arr[2], arr[3])])
    # print(arr, arr2)
    if arr1 == arr2:
        print("YES")
    else:
        print("NO") 