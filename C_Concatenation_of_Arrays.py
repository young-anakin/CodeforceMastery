t = int(input())
import heapq
for _ in range(t):
    n = int(input())
    ans = []
    trr = []
    for _ in range(n):
        arr = list(map(int, input().split(" ")))
        tmp = [arr[0] + arr[1]]
        tmp.extend(arr)
        # print(tmp)
        heapq.heappush(ans, tmp)
    
    # print(ans)
    while ans:
        val = heapq.heappop(ans)
        val = val[1:]
        trr.extend(val)
    
    print(*trr)

    # print(ans)