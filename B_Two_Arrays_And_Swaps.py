s = int(input())
for ind in range(s):
    n, k = list(map(int, input().split(" ")))
    for ind in range(1):
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))

    a.sort()
    b.sort()


    b = b[::-1]
    i, j = 0, 0
    # print(a, b)
    cp = 0
    while cp < k:
        if a[i] < b[j]:
            a[i] = b[j]
            i+=1
            j+=1
        else:
            i +=1
        cp +=1
    # print(a)
    print(sum(a[:n]))
