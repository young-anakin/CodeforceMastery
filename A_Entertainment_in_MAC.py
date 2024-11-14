t = int(input())
for _ in range(t):
    n = int(input())
    val = input()

    
    if ord(val[0]) == ord(val[-1]):
        a = 0
        b = len(val)-1
        while a < b:
            if val[a] < val[b]:
                print(val[::])
                break
            elif val[a] > val[b]:
                print(val[::-1] + val[::])
                break
            else:
                a+=1
                b-=1
                continue
        if a >= b:
            print(val)
    elif ord(val[0]) < ord(val[-1]):
        print(val)
    
    else:
        print(val[::-1] + val)