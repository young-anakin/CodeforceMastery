def solve():
    n, arr = int(input()), list(map(int, input().split()))
    ss, visited = set(), set()
    for ind in range(1, n + 1):
        visited.add(ind)
    # print(u)
    ans = [arr[-1] if arr[0] == n and sum(arr) == n + t else arr[0]]
    visited.remove(ans[0])
    ss.add(ans[0])
    for x in arr[1:]:
        if x in ss:
            ans.append(visited.pop())
        else:
            ans.append(x)
        ss.add(ans[-1])
        visited.discard(x)
    print(*ans)

for t in range(int(input())):
    solve()
