n = int(input())
for ind in range(n):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    arr.sort()

    md = (sz-1)//2
    p = arr[md]     
    cp = 1
    # print("P : ", md, "Arr : ", arr)
    for j in range(md+1, sz):
        if arr[j] == p:
            cp +=1
        else:
            break
    print(cp)