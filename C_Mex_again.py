n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()
arr[0] = 1
# print(arr)

for ind in range(n-1):
    if abs(arr[ind] - arr[ind+1]) == 0:
        continue
    else:
        arr[ind+1] = arr[ind] + 1

print(arr[-1]+1)