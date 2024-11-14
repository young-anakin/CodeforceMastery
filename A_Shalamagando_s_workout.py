n = int(input())
arr = [0,0,0]
val = list(map(int, input().split(" ")))

for ind in range(n):
    arr[ind%3] += val[ind]

mx = max(arr)
# print(mx)
if arr.index(mx) == 0:
    print("chest")
elif arr.index(mx) == 1:
    print("biceps")
else:
    print("back")
# print(arr)