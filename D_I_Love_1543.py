t = int(input())
from collections import deque
for _ in range(t):
    n, m = list(map(int, input().split(" ")))
    arr = []
    for _ in range(n):
        sub = input()
        arr.append(sub)
    
    # print(arr)
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    def inbound(i, j):
        return i >= 0 and j >= 0 and i < n and j < m
    cp = 0
    for ind in range(n):
        for j in range(m):
            queue = deque()
            visited = set()
            if arr[ind][j] == '1':
                queue.append((ind, j, '1' , "og"))
                visited.add((ind,j))
                # print(ind, j)
                while queue:
                    a, b, val, dmt = queue.popleft()   
                    og = dmt                              
                    for up, down in directions:
                        ogu = up
                        ogd = down
                        up +=a
                        down +=b
                        # print("first", up, down, val, og)
                        if og == "og":
                            if (ogu, ogd) == (0,1):
                                dmt == "r"
                            elif (ogu, ogd) == (1, 0):
                                dmt = "d"
                            elif (ogu, ogd) == (-1, 0):
                                dmt = "u"
                            elif (ogu, ogd) == (0, -1):
                                dmt = "l"
                        else:
                            if og == "u":
                                if (ogu, ogd) != (-1, 0) and (ogu, ogd) != (0, 1):
                                    continue
                                else:
                                    # print("profile", up, down, ogu, ogd)

                                    if (ogu, ogd) == (-1, 0):
                                        dmt = "u"
                                    else:
                                        dmt = "r"
                            elif og == "r":
                                if (ogu, ogd) != (0,1) and (ogu, ogd) != (1, 0):
                                    continue
                                else:
                                    if (ogu, ogd) == (1,0):
                                        dmt = "d"
                                    else:
                                        dmt = "r"
                            elif og == "l":
                                if (ogu, ogd) != (0, -1) and (ogu, ogd) != (-1, 0):
                                    continue
                                else:
                                    if (ogu, ogd) == (0, -1):
                                        dmt = "l"
                                    else:
                                        dmt = "u"
                            elif og == "d":
                                if (ogu, ogd) != (1, 0) and (ogu, ogd) != (0, -1):
                                    continue   
                                else:
                                    if (ogu, ogd) == (1, 0):
                                        dmt = "l"
                                    else:
                                        dmt = "d"                  
                        
                        if inbound(up, down) and (up, down) not in visited:
                            # print(ind, j, val, arr[up][down], dmt)

                            if val == "1":
                                if arr[up][down] == "5":
                                    queue.append((up, down, "5", dmt))
                                    visited.add((up,down))

                            elif val == "5":
                                if arr[up][down] == "4":
                                    queue.append((up, down, "4", dmt))
                                    visited.add((up,down))

                            elif val == "4":
                                if arr[up][down] == "3":
                                    # print(ind, j, arr[ind][j])
                                    cp +=1
                            # print("queue", queue)
    print(cp)
