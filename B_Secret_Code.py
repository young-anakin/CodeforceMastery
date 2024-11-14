n = int(input())
val = input()
from collections import deque
ans = deque()
if n%2 == 0:
    a = n//2-1
    b = n//2 +1
    # print(a,b)
    first = True
    # ans.append(val[n//2])
    # ans.append(val[0])
    turn = True
    for ind in range(0, n):
        if turn:
            ans.appendleft(val[ind])
            turn = False
        else:
            ans.append(val[ind])
            turn = True
    tt = "".join(ans)
    print(tt)
    # print(*ans.join(""))
else:
    a = n//2-1
    b = n//2 +1
    # print(a,b)
    first = True
    # ans.append(val[n//2])
    ans.append(val[0])
    turn = True
    for ind in range(1, n):
        if turn:
            ans.appendleft(val[ind])
            turn = False
        else:
            ans.append(val[ind])
            turn = True
    tt = "".join(ans)
    print(tt)
    # print(*ans.join(""))

    


