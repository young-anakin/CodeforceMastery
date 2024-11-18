t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    cp = Counter(arr)
    ans = 0
    for key, val in cp.items(): 
        ans += val//2
    
    print(ans)