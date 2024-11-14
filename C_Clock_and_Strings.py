t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split(" ")))
    
    if (min(a, b) < c < max(a, b)) ^ ( min(a, b) < d < max(a, b)):
        print('YES')
    else:
        print('NO')

