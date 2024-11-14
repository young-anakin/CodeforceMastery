N = int(input())
for i in range(N):
    val = input()
    if int(val[0]) + int(val[1]) + int(val[2]) == int(val[3]) + int(val[4]) + int(val[5]):
        print("YES")
    else:
        print("NO")