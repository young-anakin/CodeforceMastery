n, k = list(map(int, input().split(" ")))
arr1 =  list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))

import heapq

heap = []
heapq.heapify(heap)

visited = set()
for ind in range(len(arr1)):
    heapq.heappush(heap, (arr1[ind] - arr2[ind], arr1[ind], ind))

i = 0
ans = 0
# print(heap)
fl = True
while i != k:

    a, b, ind = heapq.heappop(heap)
    i +=1
    ans += b
    visited.add(ind)

while heap:

    a, b, ind = heapq.heappop(heap)
    if a > 0:
        break
    ans += b
    visited.add(ind)


for ind in range(n):
    if ind not in visited:
        ans += arr2[ind]

print(ans)

