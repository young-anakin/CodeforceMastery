a = int(input())
b = int(input())
c, d = min(a,b ), max(a,b)
first = []
for ind in range(c, d+1):
    n = abs(ind - d)
    first.append((n * (n+1))//2)


second = first[::-1]
mn = float("inf")
for ind in range(len(first)):
    mn = min(first[ind]+second[ind], mn)


print(mn)