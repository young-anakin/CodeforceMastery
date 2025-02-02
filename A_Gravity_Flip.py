t =  int(input())
arr = list(map(int, input().split(" ")))
mx = max(arr)
arr = arr[::-1]
# print(arr)
for ind in range(t):
    for j in range(ind + 1, t):
        if arr[ind] < arr[j]:
            diff = abs(arr[ind] - arr[j])
            arr[ind] = arr[j]
            arr[j] = abs(arr[j] - diff )

arr = arr[::-1]
print(*arr)