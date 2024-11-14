from collections import Counter
n = int(input())
for ind in range(n):
    arr = input()
    ab = Counter(arr)

    if ab['A'] > ab['B']:
        print("A")
    else:
        print("B")