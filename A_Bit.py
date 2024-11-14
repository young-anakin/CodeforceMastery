

n = int(input())
x = 0
for a in range(0, n):
    val = input()
    if '++' in val:
        x +=1
    else:
        x -=1
print(x)