n = int(input())

from heapq import heappush, heappop, heapify

heap = []

for _ in range(n):
    a, b = map(int, input().split())
    heappush(heap, (-b, -a))

score = 0
trial = 1

while trial and heap:
    b, a = heappop(heap)
    trial -= 1
    trial -= b
    score -= a

print(score)
