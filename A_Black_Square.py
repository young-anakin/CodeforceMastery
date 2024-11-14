arr = list(map(int, input().split(" ")))

s = input()

ans = 0

for ind in range(len(s)):
    ans += arr[int(s[ind])-1]

print(ans)