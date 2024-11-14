t = int(input())
for ind in range(t):
    # print(ind)
    n, m = list(map(int, input().split(" ")))
    new = []
    for ind in range(n):
        sub = input()
        new.append(sub)
    
    sets = set()
    prev = "0"
    for ind in range(m):
        for j in range(n):
            if new[j][ind] == "v" and prev == "0":
                # print(ind, j)
                sets.add("v")
                prev = "v"
                break
            elif new[j][ind] == "i" and prev == "v":
                # print(ind, j)

                sets.add("i")
                prev = "i"
                break

            elif new[j][ind] == "k" and prev == "i":
                # print(ind, j)

                sets.add("k")
                prev = "k"
                break

            elif new[j][ind] == "a" and prev == "k":
                # print(ind, j)

                sets.add("a")
                prev = "a"
                break
    if len(sets) == 4:
        print("YES")
    else:
        print("NO")
    # print(new)