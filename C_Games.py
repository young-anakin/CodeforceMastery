t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    odd, even = [], []
    for ind in arr:
        if ind %2 == 0:
            even.append(ind)
        else:
            odd.append(ind)
    even.sort()
    odd.sort()
    bob, alice = sum(odd), sum(even)
    # print(even, odd)
    oc = 0
    ec = 0
    al = True
    while len(even) > 0 or len(odd) > 0:
        if len(even) > 0 and len(odd) > 0:
            if even[-1] < odd[-1]:
                if al:
                    al = False
                    odd.pop()
                else:
                    al = True
                    oc += odd[-1]
                    odd.pop()
            else:
                if even[-1] > odd[-1]:
                    if  al:
                        al = False
                        ec += even[-1]
                        even.pop()
                    else:
                        al = True
                        even.pop()
        else:
            if al:
                if len(even) > 0:
                    ec += even.pop()
                    al = False
                else:
                    odd.pop()
                    al = False
            else:
                if len(even) > 0:
                    even.pop()
                    al = True
                else:
                    oc += odd.pop()
                    al = True
        # print(even, odd)

    if oc == ec:
        print("Tie")
    elif oc > ec:
        print("Bob")
    else:
        print("Alice")

    
        