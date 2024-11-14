import heapq
n, q , k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
visited = set()
ans = []
cp = 0
for ind in range(k):
    a, b = list(map(int , input().split(" ")))
    b-=1
    if a == 1:
        if cp < q:
            heapq.heappush(ans, (arr[b], b))
            visited.add(b)
        else:
            val = heapq.heappop(ans)
            if arr[b] < val[0]:
                heapq.heappush(ans, (val[0], val[1]))
            else:
                heapq.heappush(ans, (arr[b], b))
                visited.remove(val[1])
                visited.add(b)
        cp +=1
    else:
        if b in visited:
            print("YES")
        else:
            print("NO")