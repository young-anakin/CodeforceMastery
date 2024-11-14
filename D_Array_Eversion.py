t = int(input())
import bisect
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    mx = max(arr)
    top = arr[-1]
    if top == mx:
        print(0)
    else:
        cp = 0
        while arr:
            val = arr.pop()
            if val > top:
                top = val
                cp +=1
            
            if top == mx:
                print(cp)
                break
    
    