t = int(input())
for _ in range(t):
    s = input()
    
    ans = 0
    
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans += 1

    f = 1 if '01' in s else 0
    
    print(max(ans - f + 1, 1))
    pass