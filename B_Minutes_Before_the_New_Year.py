t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    total = 24 * 60
    yalen = a * 60
    yalen += b
    hrs = total - yalen
    print(hrs)
