t = int(input())
for _ in range(t):
    n = int(input())
    val = input()
    front = []
    opp = []
    ans = []
    for ind in range(n+1):
        ans.append(1)
    
    temp = [0]
    for ind in range(1, n+1):
        temp.append(val[ind-1])
        temp.append(ind)
    
    for ind in range(len(temp)):
        if type(ind) == int:
            if ind - 1 < 0:
                pass
            else