n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
arr.sort()

if k == 0 and  arr[0] != 1:
    print(1)
elif k == 0 and arr[0] == 1:
    print(-1)
elif n == k:
    print(arr[-1])
elif arr[k-1] == arr[k]:
    print(-1)
else:
    print(arr[k-1])
# print(arr)