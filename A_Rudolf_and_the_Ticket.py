sz = int(input())
for ind in range(sz):
    n, m , k = list(map(int, input().split(" ")))

    first = list(map(int, input().split(" ")))
    second = list(map(int, input().split(" ")))
    cp = 0
    for j in range(n):
        for b in range(m):
            if first[j] + second[b] <= k:
                cp +=1
    
    print(cp)
        