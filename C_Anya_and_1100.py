t = int(input())
target = ['1', '1', '0','0']
# 1100
for _ in range(t):
    tmp = input()
    arr = []
    for ind in range(len(tmp)):
        arr.append(tmp[ind])
    ss = set()
    n = int(input())
    # print(arr)
    fl = False
    for ind in range(len(arr)):
        if arr[ind] == "1":
            if arr[ind:ind+4] == target:
                fl = True
                ss.add(ind)
                ss.add(ind+1)
                ss.add(ind+2)
                ss.add(ind+3)
    
    # print(ss)


    for _ in range(n):
        ind, val = list(map(int, input().split(" "))) 
        ind -=1

        if fl:
            if ind not in ss :
                fl = True
            else:
                if arr[ind:ind + 4] == target:
                    for j in range(ind, ind+4):
                        ss.remove(j)
                elif arr[ind-1:ind+3] == target:
                    for j in range(ind-1, ind+3):
                        ss.remove(j)
                elif arr[ind-2:ind+2] == target:
                    for j in range(ind-2, ind+2):
                        ss.remove(j)
                elif arr[ind-3:ind+1] == target:
                    for j in range(ind-3,ind+1):
                        ss.remove(j)

                if len(ss) > 0:
                    fl = True
                else:
                    fl = False 
        arr[ind] = str(val)
        
        if arr[ind:ind + 4] == target:
            fl = True
            for j in range(ind, ind+4):
                ss.add(j)
        elif ind-1 >=0 and arr[ind-1:ind+3] == target:
            fl = True
            for j in range(ind-1, ind+3):
                ss.add(j)
        elif ind-2 >=0 and arr[ind-2:ind+2] == target:
            fl = True
            for j in range(ind-2, ind+2):
                ss.add(j)
        elif ind-3 >=0 and arr[ind-3:ind+1] == target:
            fl = True
            for j in range(ind-3, ind+1):
                ss.add(j)
        else:
            if not fl:
                fl = False
        
        if fl:
            print("YES")
        else:
            print("NO")
        
        # print(arr)


        
        #111000
        #012345
          #-




