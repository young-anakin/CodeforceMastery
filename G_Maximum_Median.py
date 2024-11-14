n, k = list(map(int, input().split(" ")))
arr = list(map(int , input().split(" ")))
arr.sort()
import math
s = n//2
new = arr[s:]
# print(s)
mn = new[0]
rem  = 0
for ind in range(len(new)):
    rem += max(new) - new[ind]

other = rem//len(new)
k -= rem
if k < 0:
    print(mn)
else:
    a = k//len(new)
    # print(bcsa)
    print(new[-1] + k//len(new))