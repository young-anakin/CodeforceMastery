t = int(input())
import bisect
for aa in range(t):
    n = int(input())
    tot = []
    for ind in range(n):
        # print("turn", ind+aa)
        arr = list(map(int, input().split(" ")))
        size, initial = arr[0], arr[1]+1

        needed = 0
        for ind in range(1, size+1):
            if initial + (ind-1) < arr[ind]:
                needed = (arr[ind] - (initial + (ind-1))) + 1
        
        # print(needed + initial)
        initial = needed + initial
        endofit = initial + size
        tot.append((initial, endofit))

    add = 0
    tot.sort(reverse=True)
    for ind in range(1, len(tot)):
        if tot[ind][1] < tot[ind-1][0]:
            add += abs(tot[ind][0] - tot[ind-1][1])
    
    print(tot, add)
    print(tot[-1][0] + add)

    # print(tot)
        # print(initial, endofit)