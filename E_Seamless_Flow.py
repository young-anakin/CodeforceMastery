t = int(input())
from collections import defaultdict, deque
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    ugraph = defaultdict(list)
    dgraph = defaultdict(list)
    seen = set()
    for _ in range(m):
        val = list(map(int, input().split(" ")))

        if val[0] == 0:
            ugraph[val[1]].append(val[2])
        else:
            dgraph[val[1]].append(val[2])

    queue = deque() 
    fl = True
    print("U", ugraph)
    print("D", dgraph)
    if dgraph:   
        queue.append(1)
        while queue:
            val = queue.popleft()
            seen.add(val)
            for ind in dgraph[val]:
                if (ind, val) in seen:
                    fl = False
                    break
                # seen.add(ind)
                # queue.append(val)
    if not(fl):
        print("NO")
        continue
    else:
        print("YES")
        continue
