n = int(input())
for _ in range(n):
    first = input()
    second = input()
    cp = 0
    fr = 0
    for ind in range(len(first)):
        if first[ind] == second[fr] and (ind+1) %2 != 0:
            cp +=1
        if cp == len(second):
            break
    
    if cp == len(second):
        print("YES")
    else:
        print("NO")