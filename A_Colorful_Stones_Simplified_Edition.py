s = input()
t = input()
pos = 1
orig = 0
for ind in range(len(t)):
    if t[ind] == s[orig]:
        pos +=1
        orig +=1
    if orig > len(s)-1:
        break

print(pos)