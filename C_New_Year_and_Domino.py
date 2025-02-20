n, m = list(map(int, input().split(" ")))
arr = []
for _ in range(n):
    sub = input()
    arr.append(sub)
t = int(input())
prefix = [[0 for i in range(m+1)] for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]
print(prefix)
for _ in range(t):
    r1, c1, r2, c2 = list(map(int, input().split(' ')))
print(arr) 