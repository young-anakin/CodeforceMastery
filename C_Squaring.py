import math

def solve():
    n = int(input())
    v = list(map(float, input().split()))

    # Reverse the vector
    v.reverse()
    while v and v[-1] == 1:
        v.pop()
    v.reverse()

    # Check for any 1 in the remaining vector
    if any(x == 1 for x in v):
        print(-1)
        return

    # Apply log(log(i)) to all elements
    v = [math.log(math.log(x)) for x in v]
    print(v)
    ans = 0
    for i in range(1, len(v)):
        need = v[i - 1] - v[i]
        if need > 1e-9:  # Equivalent to `eps` in the original
            cnt = 1 + int((need - 1e-9) / math.log(2))
            ans += cnt
            v[i] += cnt * math.log(2)

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
