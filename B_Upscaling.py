n = int(input())
for ind in range(n):
    p = int(input())
    arr = []
    ha = ["##"]
    v = ['..']
    turn = True    

    for i in range(p):
        sub = []
        for j in range(p):
            if turn:
                sub.extend(ha)
                turn = not(turn)
            else:
                sub.extend(v)
                turn = not(turn)
        print("".join(sub))
        # print(turn)
        if p %2 != 0:
            turn = turn
        else: 
            turn = not(turn)
        print("".join(sub))
        
    # print('k')
