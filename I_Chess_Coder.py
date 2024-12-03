n = int(input())

ans = []
for i in range(n):
    ll = ["."]*n
    ans.append(ll)

sset = set()
count = 0

for i in range(n):
    for j in range(n):
        if (i,j) not in sset:
            ans[i][j] = "C"
            count += 1
            sset.add((i+1,j))
            sset.add((i-1,j))
            sset.add((i,j+1))
            sset.add((i,j-1))

print(count)
for val in ans:
    print("".join(val))

