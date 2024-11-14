from collections import Counter
n = int(input())
for ind in range(n):
    val = input()
    cp = Counter(val)
    even = 0
    for key, values in cp.items():
        if values %2 == 0 or (values % 2 == 1 and values > 1):
            even +=1
    if even > 1:
        print("YES")
    else:
        print("NO")