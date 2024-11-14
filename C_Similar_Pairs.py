t = int(input())
import heapq
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    # print(arr)

    together = 0

    val = arr[0]
    check = []

    heapq.heapify(arr)

    while arr:
        if len(arr) >= 2:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            # print("vals", x, y)
            if abs(x-y) == 1:
                # print("Ya")
                # heapq.heappop(arr)
                # heapq.heappop(arr)
                together +=1
            else:
                # print("NO")
                check.append(x)
                heapq.heappush(arr, y)
        else:
            check.append(heapq.heappop(arr))



    # print("check", check)
    odd, even = [], []
    for ind in check:
        if ind % 2 == 0:
            even.append(ind)
        else:
            odd.append(ind)
    
    # print(even, odd)
    evenCP = len(even) %2 
    oddCP = len(odd) %2 

    # print(evenCP, oddCP)
    # print(together)
    # print(odd, even)

    if evenCP == oddCP == 0:
        print("YES")
    else:
        if together >= 1:
            print("YES")
        else:
            print("NO")