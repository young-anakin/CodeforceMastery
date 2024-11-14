n , a, b = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
arr.sort()
# print(arr)
mx = arr[b-1]
print(abs(mx - arr[b]))