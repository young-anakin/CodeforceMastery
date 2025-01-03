
n = int(input())
arr = list(map(int, input().split(" ")))
chance = True

tt = sorted(arr)

stack = []
cp = 0
fl = True
first = 0
last = 0
for ind in range(len(arr)):
    if arr[ind] != tt[ind]:
        if fl:
            first = ind
            fl = False
        else:
            last = ind
# print(arr[0:first] + list(reversed(arr[first:last+1])) + arr[last+1:])
if arr[0:first] + list(reversed(arr[first:last+1])) + arr[last+1:] == tt:
    print("yes")
    print(first+1, last+1)
else:
    print("no")
# print(first, last)
