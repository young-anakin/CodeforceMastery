from collections import Counter
n = int(input())
for i in range(n):
    size = int(input())
    arr = list(map(int, input().split(" ")))
    x = Counter(arr)
    flag = False
    for a, b in x.items():
        if b >= 2:
            flag = True
            print("NO")
            break
    if flag == False:
        print("YES")
