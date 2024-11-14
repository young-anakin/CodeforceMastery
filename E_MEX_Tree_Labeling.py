from collections import defaultdict, deque
import heapq
t = int(input())
dd = defaultdict(int)
tree = defaultdict(list)
arr = []
for _ in range(t-1):
    u, v = list(map(int, input().split(" ")))


    arr.append((u,v))
    dd[u] +=1
    dd[v] +=1


ds = defaultdict(int)
for ind in range(t-1):
    u, v = arr[ind]
    if dd[u] >= dd[v]:
        dd[u] +=1
        ds[u] +=1
        tree[v].append((min(u, v), max(u,v)))
    else:
        ds[v] +=1 
        dd[v] +=1
        tree[u].append((min(u, v), max(u,v)))




# print(arr)
queue = deque()

mn = min(dd.values())
# print(mn)
# sorted(dd.items(), key = lambda x:x[1])
art = []
for key, values in dd.items():
     art.append((values, key))
    
print(art)
heapq.heapify(art)
while art:
     val = heapq.heappop(art)
     print(val)
     queue.append(val[1])
    #  print(queue)
print(dd)
print(tree)
ans = defaultdict(lambda:-1)
visited = set()
# for key, val in dd.items():
    
#     queue.append(key)
print(queue)

i = 0
print("tree", tree)
while queue:
    val = queue.popleft()
    for ind in tree[val]:
        print(ind, val)
        ans[ind] = i
        i +=1
        dd[ind[0]] -=1
        dd[ind[1]] -=1
        # print(dd)
        if ind[0] != val:
            # if dd[ind[0]] == 0:
                queue.append(ind[0])
        elif ind[1] != val:
            # if dd[ind[1]] == 0:
                queue.append(ind[1])

# print(ds)
for val in arr:
    print(ans[val])

# print(dd)