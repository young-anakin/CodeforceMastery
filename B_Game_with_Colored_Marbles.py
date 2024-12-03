t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    cp = Counter(arr)
    alice, bob = 0,0
    sorted_dict = dict(sorted(cp.items(), key=lambda item: item[1]))
    turn = True
    for key, val in sorted_dict.items():
        if turn:
            if val == 1:
                alice +=2
            else:
                alice +=1
            turn = False
        else:
            if val == 1:
                bob +=1
            else:
                bob +=1
                alice +=1
            turn = True

    # print(sorted_dict)
    print(alice)