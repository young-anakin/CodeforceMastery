n, m = list(map(int, input().split(" ")))
arr = []
from collections import defaultdict, deque
import heapq
roads = defaultdict(list)
train = defaultdict(list)
railways = set()
for _ in range(m):
    aa = list(map(int, input().split(" ")))
    railways.add((aa[0], aa[1]))
    railways.add((aa[1], aa[0]))
    train[aa[0]].append(aa[1])
    train[aa[1]].append(aa[0])
    arr.append(aa)


for ind in range(1, n+1):
    for j in range(ind+1, n+1):
        if (ind, j) not in railways:
            roads[ind].append(j)
            roads[j].append(ind)
if not roads or not train:
    print(-1)
else:
    # print(roads)
    heap = deque()
    heap.append((1,0))
    # heap = [(1,0)]
    visited = set()
    dd = defaultdict(int)
    for ind in range(1, n+1):
        dd[ind] = float("inf")

    dd[1] = 0
    # print(dd)
    isTrain = False
    for ind in train[1]:
        if ind == n:
            isTrain = True
            break



    # print(isTrain)
    if not(isTrain):
        isDest = False
        ans = 0
        while heap:
            a,b = heap.popleft()
            if a == n:
                isDest = True
                ans = b
                break
            if a in visited:
                continue
            visited.add(a)

            for child in train[a]:
                heap.append((child, b+1))
        if isDest:
            print(b)
        else:
            print(-1)
    else:
        isDest = False
        ans = 0
        while heap:
            a,b = heap.popleft()
            if a == n:
                isDest = True
                ans = b
                break
            if a in visited:
                continue
            visited.add(a)

            for child in roads[a]:
                heap.append((child, b+1))
        if isDest:
            print(b)
        else:
            print(-1)


        #     for child in 
        # heapq.heappush()
    # print(isRoad)
    # print(train)
    # print(arr)