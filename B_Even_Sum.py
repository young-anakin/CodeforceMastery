t = int(input())
for _ in range(t):
    a = int(input())
    arr = list(map(int, input().split(" ")))
    sm = sum(arr)
    
    if sm%2 == 0:
        print(0)
    else:
        arr.sort()
        
        mx = float("inf")

        for ind in arr:
            cp = 0
            fl = True
            if ind %2 == 0:
                fl = False

            if fl:
                while (fl):
                    cp +=1
                    ind = ind//2

                    if ind % 2 == 0:
                        fl = False
            else:
                while not(fl):
                    cp +=1

                    ind = ind //2

                    if ind %2 ==1 :
                        fl = True
            
            mx = min(mx, cp)

        print(mx)

