n = int(input())
from collections import defaultdict
arr = list(map(int, input().split(" ")))
sm = sum(arr)/ (n/2)
# print(sm)
chosen = set()
for ind in range(n):
    if ind not in chosen:
        for j in range(ind, n):
            # print(sm, arr[ind], arr[j])
            if abs(sm - arr[ind]) == arr[j] and j not in chosen and ind != j:
                chosen.add(j)
                tmp = []
                tmp.extend([ind+1, j+1])
                tmp.sort()
                print(*tmp)
                break
        if len(chosen) == n//2:
            break