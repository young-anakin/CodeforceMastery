def HolidayOfEquality(n, arr):
    arr.sort()
    i = 0
    j = arr[n-1]
    count = 0
    for a in range(0, n):
        count += j - arr[a]
    return count

x = int(input())
arr = list(map(int, input().split()))
print(HolidayOfEquality(x, arr))
