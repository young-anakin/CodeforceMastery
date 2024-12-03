##TRUST YOUR INTUITTON
from collections import defaultdict
import sys
from random import randint

def mapIn(dataType = int):return map(dataType , sys.stdin.readline().strip().split())
def stIn(): return sys.stdin.readline().strip()

def solve():
    n,k = mapIn()
    x = randint(1 , int(1e6))

    bs = defaultdict(int)
    for _ in range(k):
        a,b = mapIn()
        bs[a^x] += b
    
    lst = []
    for i in bs.keys():
        lst.append(bs[i])
    
    lst.sort(reverse=True)

    print(sum(lst[:n]))
     
     


testcase = 1
T = int(input()) if testcase else 1
for _ in range(T):
    solve()