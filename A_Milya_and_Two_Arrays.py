t = int(input())
for _ in range(t):
    n = int(input())
    arrA = list(map(int, input().split(" ")))
    arrB = list(map(int, input().split(" ")))
    smA, smB = set(arrA), set(arrB)
    # print(len(smA), len(smB))
    if len(smA) + len(smB) <= 3:
        print("NO")
    else:
        print('YES')