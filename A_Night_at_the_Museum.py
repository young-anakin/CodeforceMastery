s = input()
let = "abcdefghijklmnopqrstuvwxyz"
cp = 0
s = 'a' + s
print(s)
for ind in range(len(s)):
    cp += min(abs((let.index(s[ind]) + let.index(s[ind+1]))), 26 - abs(let.index(s[ind] + let.index(s[ind+1]))))

print(cp)