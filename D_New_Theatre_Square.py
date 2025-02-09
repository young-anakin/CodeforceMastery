t = int(input())
for _ in range(t):
    n, m, one, two = list(map(int, input().split(" ")))
    arr = []
    for _ in range(n):
        val = input()
        arr.append(val)
    tot = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue
            if arr[i][j] == ".":
                # print((i, j))
                if j+1 == m:
                    tot += one
                else:
                    if arr[i][j+1] == ".":
                        priceA, priceB = one*2, two
                        # print(priceA, priceB, (i, j))
                        if priceA <= priceB:
                            tot += one
                        else:
                            tot += priceB
                            visited.add((i, j+1))
                        # print(/tot)
                        # print(visited)
                    else:
                        tot += one
            # print(i, j, "=", tot, visited)

    print(tot)