t = int(input())
import heapq
for _ in range(t):
    n, m = list(map(int, input().split(" ")))


    tot = []
    for _ in range(n):
        val = list(map(int, input().split(" ")))
        heapq.heappush(tot, (-1 * sum(val), val))
    
    fin = []
    while tot:
        a, b = heapq.heappop(tot)
        fin.extend(b)

    sm = 0
    pf = 0
    # print(fin)
    for ind in range(len(fin)):
        sm += pf
        sm += fin[ind]
        pf += fin[ind]
    print(sm)
    
    



