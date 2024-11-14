n = int(input())
S = input()
T = input()
from collections import defaultdict
dd = defaultdict(tuple)
tot = 0
ss = set()
for ind in range(n):
    if S[ind] != T[ind]:
        dd[(ind, S[ind])] = (ind, T[ind])
        set.append(T[ind])
        tot +=1


for key, val in dd.items():

print(dd)