t = int(input())
for _ in range(t):
    n = int(input())
    ans = [(ind + ind+1) for ind in range( n)]
    print(*ans)