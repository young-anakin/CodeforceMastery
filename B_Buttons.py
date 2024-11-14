n = int(input())
tot = 0
# tot += n-1
tot += n
# tot += 2 * (n-2)
for ind in range(1, n):
    tot += ind * (n - ind)
print(tot)