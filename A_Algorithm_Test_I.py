t = int(input())
n = list(map(int, input().split(" ")))
ss = set(n)
val = list(ss)
i = 1
for ind in range(1, len(val)+1):
    i *= ind

print(i)