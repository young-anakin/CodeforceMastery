n = int(input())
cp = n
tot = 0
for ind in range(1, n+1):
    rest = cp - ind
    if rest % ind == 0:
        tot +=1

print(tot-1)