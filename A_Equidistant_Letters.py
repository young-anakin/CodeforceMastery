t = int(input())
from collections import Counter
for _ in range(t):
    val = input()
    cp = Counter(val)
    arr = []
    for key, val in cp.items():
        for _ in range(val):
            arr.append(key)
    
    print("".join(arr))

    

        
