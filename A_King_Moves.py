def KingMoves(n):
    a = n[0]
    b = n[1]
    if a == 'a' or a == 'h':
        if b == "1" or b == "8":
            return 3
        else:
            return 5
    elif b == "1" or b == "8":
        return 5
    return 8

        
n = str(input())
print(KingMoves(n))
