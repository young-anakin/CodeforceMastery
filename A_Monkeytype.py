t = int(input())
from collections import Counter
for _ in range(t):
    alph = input()
    cp = Counter(alph)
    str = input()
    ans = 0
    # print(alph.index('a'))
    for ind in range(len(str)-1):
        ans += abs(alph.index((str[ind])) -  (alph.index(str[ind+1])) )
    
    print(ans)