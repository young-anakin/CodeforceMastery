t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    val = input()
    cp = Counter(val)
    mx = max(cp.values())
    need = ""
    for key, va in cp.items():
        if va == mx:
            need += key
            break

    arr = [val[i] for i in range(n)]
    for i in range(n):
        if arr[i] != need:
            arr[i] = need
            break
    print("".join(arr))
    # print(need)
