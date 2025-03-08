t = int(input())
from collections import defaultdict, deque
for _ in range(t):
    n = int(input())
    # on = defaultdict(int)
    # off = defaultdict(int)
    onqueue = deque()
    offqueue = deque()
    unique = 1
    onFlag, offFlag = False, False
    onCp, offCp = 0, 0
    val = input()
    ans = 1
    arr = []
    if val[0] == "0":
        offFlag = True
        offCp +=1
        offqueue.append(1)
    else:
        onCp = 1
        onFlag = True  
        onqueue.append(1)
    arr.append(1)   
    # queue.append(1)   
    for i in range(1, n):
        if val[i] == "0":
            if onFlag == False:
                ans +=1
                offqueue.append(unique+1)
                arr.append(unique + 1)
                unique +=1
            else:
                onCp -=1
                if onCp == 0:
                    onFlag = False
                tmp = onqueue.popleft()
                arr.append(tmp)
                offqueue.append(tmp)
            offFlag = True
            offCp +=1
        else:
            if offFlag == False:
                ans +=1
                onqueue.append(unique + 1)
                arr.append(unique + 1)
                unique +=1
            else:
                offCp -=1
                if offCp == 0:
                    offFlag = False
                tmp = offqueue.popleft()
                arr.append(tmp)
                onqueue.append(tmp)
            
            onFlag = True
            onCp +=1
    
    print(ans)
    print(*arr)

