a, b = list(map(int, input().split(" ")))
acount, bcount, draw = 0,0, 0
for ind in range(1, 7):
    # print(ind)
    # print(a-ind, b-ind)
    if abs(a - ind) > abs(b-ind):
        bcount +=1
    elif abs(a-ind) == abs(b-ind):
        draw +=1
    else:
        acount +=1
    # print(acount, draw, bcount)    
    
print(acount, draw, bcount)