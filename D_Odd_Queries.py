import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
t = int(input())
for ind in range(t):
    q, n = get_ints()
    arr = list(map(int, input().split(" ")))

    ps = [0]
    for ind in range(len(arr)):
        ps.append(ps[-1] + arr[ind])
    # ps.pop(0)
    mx = ps[-1]
    for j in range(n):
        a, b, c = get_ints()
        val = mx -  (ps[b] - ps[a-1])
        # print(val)
        val = val + ((b-a)+1)*c

        # print(ps, val)
        if val %2 == 0:
            print("NO")
        else:
            print("YES")