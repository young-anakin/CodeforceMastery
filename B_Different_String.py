def rearrange_string(s):
    n = len(s)
    if n == 1:
        return "NO"

    if len(set(s)) == 1:
        return "NO"

    return s[1:] + s[0]

t = int(input())

for _ in range(t):
    s = input().strip()
    result = rearrange_string(s)
    if result == "NO":
        print("NO")
    else:
        print("YES")
        print(result)
