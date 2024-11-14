t = int(input())
for _ in range(t):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    arr.reverse()
    ans = []
    visited = set()
    for i in arr:
        if i not in visited:
            ans.append(i)
            visited.add(i)
    ans.reverse()
    print(*ans)