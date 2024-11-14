t = int(input())
arr = []
from collections import defaultdict, deque
dd = defaultdict(deque)
moves = defaultdict(int)
remove = defaultdict(int)
for _ in range(t):
    ll = list(map(str, input().split(" ")))
    if ll[0] == "insert":
        if moves[ll[2]] == 0:
            dd[(ll[2], remove[ll[2]])].append((ll[1], moves[ll[1]]))
        else:
            dd[(ll[2], remove[ll[2]])].appendleft((ll[1], moves[ll[1]]))
        moves[ll[1]] +=1
        # moves[ll[2]] +=1
    else:
        # dd[(ll[1], remove[ll[1]])].append("remove")
        remove[(ll[1], moves[ll[1]])] +=1

ab = []
ans = []
# for key, values in dd.items():
#     ab.append(key)

#     queue = deque()
#     queue.append(dd[0][1])
#     while 
# print()
print(dd)
print("----------")
print(remove)