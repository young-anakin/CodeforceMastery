t = int(input())
import bisect
for _ in range(t):
    r, g, b = list(map(int, input().split(" ")))
    red = list(map(int, input().split(" ")))
    green = list(map(int, input().split(" ")))
    blue = list(map(int, input().split(" ")))
    red.sort()
    green.sort()
    blue.sort()

    # print(green, blue)
    mn = float("inf")
    # red
    for ind in range(r):
        sm = 0
        first = bisect.bisect_right(green, red[ind])
        # print(red[ind])
        if first == g:
            greenball = green[-1]
        else:
            greenball = green[first]

        second = bisect.bisect_right(blue, red[ind])
        if second == b:
            blueball = blue[-1]
        else:
            blueball = blue[second]
        
        sm = ((greenball - blueball) ** 2) + ((greenball - red[ind]) ** 2) + ((red[ind] - blueball) ** 2)
        mn = min(sm, mn)


    for ind in range(g):
        sm = 0
        first = bisect.bisect_right(red, green[ind])
        # print(red[ind])
        if first == r:
            greenball = red[-1]
        else:
            greenball = red[first]

        second = bisect.bisect_right(blue, green[ind])
        if second == b:
            blueball = blue[-1]
        else:
            blueball = blue[second]
        
        sm = ((greenball - blueball) ** 2) + ((greenball - green[ind]) ** 2) + ((green[ind] - blueball) ** 2)
        mn = min(sm, mn)


    for ind in range(b):
        sm = 0
        first = bisect.bisect_right(green, blue[ind])
        # print(red[ind])
        if first == g:
            greenball = green[-1]
        else:
            greenball = green[first]

        second = bisect.bisect_right(red, blue[ind])
        if second == r:
            blueball = red[-1]
        else:
            blueball = red[second]
        
        sm = ((greenball - blueball) ** 2) + ((greenball - blue[ind]) ** 2) + ((blue[ind] - blueball) ** 2)
        mn = min(sm, mn)
    
    print(mn)
