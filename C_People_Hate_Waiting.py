def solve():
    s = input()
    a = [0] * 100005
    a[1] = 0
    for i in range(1, len(s)):
        a[i + 1] = a[i] + (s[i - 1] == s[i])

    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        print(a[y] - a[x])

if __name__ == "__main__":
    solve()
