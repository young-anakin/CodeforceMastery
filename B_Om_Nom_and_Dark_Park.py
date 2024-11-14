from collections import defaultdict, deque
dd = defaultdict(int)
n = int(input())
arr = list(map(int, input().split(" ")))
fl = True
i = 1
for ind in arr:
    if fl:
        dd[(i, i*2)] = ind
        fl = False
    else:
        dd[(i, (i*2)+1)] = ind
        fl = True
        i +=1

queue = deque()
queue.append((1,2, dd[(1,2)]))
queue.append((1,3 , dd[(1,3)]))
mx = 0
while queue:
    val = queue.popleft()
    # val[2] += dd[(val[0],val[1])]
    if val[1] >= 2 ** n:
        mx = max(mx, val[2])
    else:
        queue.append((val[1], val[1]*2, dd[val[1], val[1]*2] + val[2]))
        queue.append((val[1], (val[1]*2) + 1, dd[val[1], (val[1]*2)+1] + val[2]))

cp = 0
sub = defaultdict(int)    
zz = defaultdict(int)
# print(mx)
for ind in range(1, (2**n)):
    tmpMax = 0
    queue.append((ind, ind*2, dd[(ind, ind*2)]))
    # print(queue)
    while queue:
        val = queue.popleft()
        if val[1] >= 2 ** n:
            tmpMax = max(tmpMax, val[2])
            # print(ind, tmpMax)
        else:
            queue.append((val[1], val[1]*2, dd[val[1], val[1]*2] + val[2]))
            queue.append((val[1], (val[1]*2) + 1, dd[val[1], (val[1]*2)+1] + val[2]))
    sub[(ind, ind*2)] += mx - (tmpMax + zz[ind])
    # print((ind, ind*2), sub[(ind, ind*2)], zz[ind])
    zz[ind*2] = sub[(ind, ind*2)] + dd[(ind, (ind*2))] + zz[ind]
    # print(ind, tmpMax)
    tmpMax = 0
    queue.append((ind, (ind*2)+1, dd[(ind, (ind*2)+1  )]))
    # print(queue)
    while queue:
        val = queue.popleft()
        if val[1] >= 2 ** n:
            tmpMax = max(tmpMax, val[2])
        else:
            queue.append((val[1], val[1]*2, dd[val[1], val[1]*2] + val[2]))
            queue.append((val[1], (val[1]*2) + 1, dd[val[1], (val[1]*2)+1] + val[2]))
    # sub[(ind*2)+1] += mx- tmpMax

    sub[(ind, (ind*2)+1)] += mx - (tmpMax + zz[ind])
    # print((ind, ind*2 + 1), sub[(ind, ind*2 + 1)])

    zz[(ind*2)+1] = sub[(ind, (ind*2)+1)] + dd[(ind, (ind*2)+1)] + zz[ind]
    # print(ind, tmpMax)

ans = 0
# print("xx", zz)

for key, value in sub.items():
    # print(key, value)
    ans += value
print(ans)
        