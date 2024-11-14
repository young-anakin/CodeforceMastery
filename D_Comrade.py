n, m , z = list(map(int, input().split(" ")))
first, second = [], []
ind = n
while ind <= z:
    first.append(ind)
    ind  += n

ind = m
while ind <= z:
    second.append(ind)
    ind  += m
# print(first, second)

ff = set(first)
ss = set(second)
cp = 0
for ind in first:
    if ind in ss:
        cp +=1

print(cp)
ll = set()