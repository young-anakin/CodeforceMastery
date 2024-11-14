n = int(input())
for ind in range(n):
    val = int(input())
    first = (int(str(val)[0])-1 )* 10
    size = len(str(val))
    # print(first, size)
    for ind in range(1,size+1):
        first += ind
    print(first)
