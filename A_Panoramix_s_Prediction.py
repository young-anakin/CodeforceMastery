prime = []

for ind in range(1, 50):
    fl = True
    for j in range(2, ind-1):
        if ind % j == 0:
            fl = False
            break
    if fl == True:
        prime.append(ind)

x, y = map(int, input().split(" "))
z = prime.index(x)
# print(z, len(prime)-1)
if z == len(prime)-1:
    print("NO")
elif prime[z+1] == y:
    print("YES")
else:
    print("NO")