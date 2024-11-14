from collections import Counter
n = int(input())
for _ in range(n):
    val = input()
    cp = Counter(val)
    # print(cp)
    if val != val[::-1]:
        print(len(val))
    elif len(cp) == 1:
        print(-1)
    else:
        mn = min(cp.values())
        print(len(val) - 1)