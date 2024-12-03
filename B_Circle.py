t = int(input())
arr = list(map(int, input().split(" ")))
import heapq
n = len(arr)
arr.extend(arr)

a, b = 0,0
mn = float("inf")

for ind in range(1,n+1):
    if abs(arr[ind] - arr[ind-1]) < mn:
        a, b = ind, ind-1
        mn = min(mn, abs(arr[ind] - arr[ind-1]) )
    
a +=1
b +=1

if a == n+1:
    a = 1

if b == n+1:
    b = 1
print(a,b)
