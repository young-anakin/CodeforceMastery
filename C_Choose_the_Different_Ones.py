n = int(input())
for ind in range(n):
    size = list(map(int, input().split(" ")))
    first = list(map(int, input().split(" ")))
    second = list(map(int, input().split(" ")))

    ab = set(first)
    cd = set(second)

    first = list(ab)
    second = list(cd)

    first.sort()
    second.sort()

    ms = first
    ms.extend(second)
    ms = set(ms)
    ms = list(ms)
    # print(ms)
    if first[(size[2]//2)-1] <= size[2] and second[(size[2]//2)-1] <= size[2]:
        

        
        if sum(ms[:size[2]]) == (size[2]* (size[2]+1))//2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    