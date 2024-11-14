t = int(input())
for _ in range(t):
    val = list(map(int, input().split(" ")))
    print(min(val), max(val))