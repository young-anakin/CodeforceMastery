n, t = list(map(int, input().split(" ")))

arr = list(map(int, input().split(" ")))

import heapq

heap = list()
heapq.heapify(heap)

for ind, val in enumerate(arr):
    heapq.heappush(heap, ((ind + 1) + val, val, ind+1))

sm = 0
extra = 0

count = 1
items, cost = 0,0
last = 0
print(heap)
while heap:
    a, b, c = heapq.heappop(heap)
    sm += b
    extra += c
    # print("cost", sm + (count * extra))
    if sm + (count * extra) <= t:
        items = count
        cost = sm + (count * extra)
        count +=1
print(items, cost)
# print(heap)