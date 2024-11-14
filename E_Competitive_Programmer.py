t = int(input())
from collections import Counter
for _ in range(t):
    val = input()
    cp = Counter(val)
    if len(val) == cp['0']:
        print("red")
    elif cp['0'] == 0:
        print("cyan")
    else:
        tot = 0
        even = 0
        for ind in val:
            if int(ind) %2 == 0 and int(ind) != 0:
                even +=1
            tot += int(ind)

        if tot % 3 == 0 and (even > 0 or cp['0'] > 1):
            print("red")
        elif even == 0:
            print("cyan")
        else:

            print("cyan")