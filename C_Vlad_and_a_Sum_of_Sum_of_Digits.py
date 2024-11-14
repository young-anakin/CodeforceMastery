n = int(input())
ans = [0]
for ind in range(200001):
    ans.append(ans[-1] + sum(map(int, str(ind))))
for ind in range(n):
    inp = int(input())
    print(ans[inp+1])
