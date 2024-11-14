n, k = list(map(int, input().split(" ")))
i = 1
tot = 0
cp = 0
arr = []
import bisect
while tot <= 10**9 + 1:
    tot +=i
    cp +=1
    i +=1
    arr.append(tot)
# arr = [1,2,3,12]
# print(arr)
x = bisect.bisect_left(arr, k)
new = []
i = 1
for ind in range(len(arr)):
    new.append(i + arr[ind])
    i +=1

print(new)
if k == 0:
    print(new)
    x = bisect.bisect_left(new, k)
    print(n - (new.index(n)+1))
# if k == 0:
#     print(n//2 + 1)
# else:
else:
# x-=1
    print(arr[x] - k )