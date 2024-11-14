n, m = list(map(int, input().split(" ")))
from collections import defaultdict, deque
dd = defaultdict(list)
# child = defaultdict(set)
for _ in range(m):
    a,b,c = list(map(int, input().split(" ")))
    dd[a].append((b,c))
    dd[b].append((a,c))
    # child[a].add(b)
    # child[b].add(a)
q = int(input())
for _ in range(q):
    coco = defaultdict(int)

    u, v = list(map(int, input().split(" ")))

    queue = deque()
    # print(dd)
    cp = 0
    visited = set()
    for ind in dd[u]:
        queue.append(ind)
        tmp = [u, ind[0]]
        if ind[0] == v:
            coco[ind[1]] +=1
        tmp.sort()
        visited.add((tuple(tmp), ind[1]))
    # print(queue)
    while queue:
        ind, color = queue.popleft()
        for a,b in dd[ind]:
            tmp = [a, ind]
            tmp.sort()
            if (tuple(tmp), color) not in visited and color == b:
                if a == v:
                    coco[color] +=1
                    continue
                queue.append((a,b))
                visited.add((tuple(tmp), b))

    
        


    print(len(coco))