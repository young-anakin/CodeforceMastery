from collections import Counter
n = int(input())
for a in range(n):
    size = int(input())
    arr = list(map(int, input().split(" ")))
    bs = Counter(arr)
    for key, values in bs.items():
        if values == 1:
            print(arr.index(key)+1) 
        