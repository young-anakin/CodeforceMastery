import bisect

arr = [1,2,3,4]

x = bisect.bisect_left(arr, 4)
print(x)