n, m , k = list(map(int, input().split(" ")))
special = list(map(int, input().split(" ")))
from collections import defaultdict, deque
dd = defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    dd[a].append(b)
    dd[b].append(a)

mx = -1 * float("inf")
the_one = 0
# print(dd)
for ind in special:
    queue = deque()
    visited = set()
    queue.append(ind)
    # tot = 0
    # print("queue", queue)
    while queue:
        val = queue.popleft()
        visited.add(val)
        for j in dd[val]:
            if j not in visited:
                visited.add(j)
                queue.append(j)
                # tot +=1
    if len(visited) >= mx:
        mx = len(visited)
        the_one = ind
    # print(visited, the_one)

# print(the_one)
neg = set()
op = 0

# neg.update(special)
visited = set()
for ind in special:
    allez = set()
    tot = 0
    if ind != the_one:
        queue = deque()
        queue.append(ind)
        tot += len(dd[ind])
        allez.add(ind)
        # visited.add(ind)
        while queue:
            val = queue.popleft()
            for i in dd[val]:
                if i not in allez:
                    tot += len(dd[i])
                    allez.add(i)
                    # visited.add(i)
                    queue.append(i)
        
    neg.update(allez)
    tt = len(allez)-1
    op += (tt * (tt+1))/2
    op -= tot//2

cp = len(neg)

ov = n - cp
ov -=1
ovv = (ov * (ov+1))/2
ov = int(ovv)
ov += op
# print(ov)
# print(neg)

tot = 0
for ind in range(1, n+1):
    if ind not in neg:
        tot += len(dd[ind])

print(int(ov - tot//2))
# tot = len(dd[the_one])
# tot +=1
# cp = 0
# for ind in range(1, n+1):
#     if ind not in neg:
#         cp += tot
#         tot +=1

# print(cp)