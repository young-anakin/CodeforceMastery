import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    ss = set()

    heap = list()
    heapq.heapify(heap)
    visited = set()
    for ind in range(n):
        if arr[ind] % 2 == 0 and arr[ind] not in visited:
            heapq.heappush(heap, -1 * arr[ind])
            visited.add(arr[ind])
    
    cp = 0
    # print(heap)
    while heap:
        val = -1 * heapq.heappop(heap)
        new = val / 2
        # print(val, new)
        if new % 2 == 0:
            if new not in visited:
                heapq.heappush(heap, -1 * new)
                visited.add(new)
            cp +=1
        else:
            cp +=1
        # print(heap)
    print(cp)
