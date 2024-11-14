t = int(input())
from collections import defaultdict

for _ in range(t):
    tt = defaultdict(int)
    n = int(input())
    fl = False
    mn = 101
    if n < 3:
        if n == 1:
            print(1)
        elif n == 2:
            print(2)
    elif n%5 == 0:
        print(0)
    elif n % 3 == 0:
        print(0)
    elif n % 8 == 0:
        print(0)
    else:
        xx = n
        while xx >= 0:
            xx -= 5
            if xx >= 0 and xx%3 == 0:
                fl = True
                # print("ja", xx)
                break
        xx = n
        if not fl:
            while xx >= 0:
                xx -=3
                if xx >= 0 and xx%5 == 0:
                    fl = True
                    break
        
        if fl:
            print(0)
        else:
            print(1)