n = int(input())
val = set()
que = input()
for i in range(n):
    val.add(que[i].lower())

if len(val) == 26:
    print("YES")
else:
    print("NO")