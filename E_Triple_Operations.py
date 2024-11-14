from math import ceil
import sys
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    a,b = dmsllinp(int)

    arr3 = [3**i for i in range(1,13)]
    
    mino = min(a,b)
    maxo = max(a,b)

    ans = 0

    x = mino
    while x:
        x = x//3
        ans+=2 


    mino+=1

    for i in range(12):
        if mino<=(arr3[i])<=maxo:
            ans+=(arr3[i] - mino)*(i+1)
            mino = arr3[i]
        elif arr3[i] > maxo and mino <= maxo:
            ans+=(maxo-mino+1)*(i+1)
            break
    
    return ans







    

for _ in range(dmslinp(int)):
    print(solve())
