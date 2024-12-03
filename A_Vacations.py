t = int(input())
from collections import defaultdict
arr = list(map(int, input().split(" ")))
memo = {}

def dp(ind, contest, gym):
    if ind >= t:
        return 0

    if (ind, contest, gym) not in memo:
        if arr[ind] == 0:
            memo[(ind, contest, gym)] = dp(ind + 1, True, True)
        
        elif arr[ind] == 1:
            if contest:
                memo[(ind, contest, gym)] = 1 + dp(ind + 1, False, True)
            else:
                memo[(ind, contest, gym)] = dp(ind + 1, True, True)

        elif arr[ind] == 2:
            if gym:
                memo[(ind, contest, gym)] = 1 + dp(ind + 1, True, False)
            else:
                memo[(ind, contest, gym)] = dp(ind + 1, True, True)

        elif arr[ind] == 3:
            if gym and contest:
                memo[(ind, contest, gym)] = max(1 + dp(ind + 1, True, False), 1 + dp(ind + 1, False, True))
            elif gym:
                memo[(ind, contest, gym)] = 1 + dp(ind + 1, True, False)
            elif contest:
                memo[(ind, contest, gym)] = 1 + dp(ind + 1, False, True)
        
    return memo[(ind, contest, gym)]

x = dp(0, True, True)
print(len(arr) - x)
