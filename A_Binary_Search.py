n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
query = list(map(int, input().split(" ")))
def binarySearch(val):
    l = 0
    r = len(arr)-1
    md = (l+r)//2
    while l <= r:
        if arr[md] == val:
            return "Yes"
        elif arr[md] < val:
            l = md+1
        else:
            r = md-1
    return "No"

for ind in range(k):
    print(binarySearch(query[ind]))