from collections import defaultdict
n = int(input())
for ind in range(n):
    size = int(input())
    s  = input()
    visited = defaultdict(int)
    curr = s[0]
    flag = True
    s += "0"
    for a in range(len(s)-1):
        if s[a] != s[a+1]:
            visited[s[a]] +=1
        if visited[s[a]] > 1:
            flag = False
            break
    # print(visited)
    if flag == False:
        print("NO")
    else:
        print("YES")
