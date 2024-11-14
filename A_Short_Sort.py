n = int(input())
real = "abc"
for ind in range(n):
    val = input()
    if val[0] == real[0] or val[1] == real[1] or val[2] == real[2]:
        print("YES")
    else:
        print("NO")