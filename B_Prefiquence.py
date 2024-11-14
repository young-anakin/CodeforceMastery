t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    first = input()
    second = input()
    cp = 0
    j = 0
    for i in range(b):
        # print(j)
        if j < a and first[j] == second[i]  :
            cp +=1
            j +=1
    print(cp)