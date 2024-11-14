t = int(input())
import math
for _ in range(t):
    a = input()
    b = input()

    x = math.lcm(len(a), len(b))
    y, z = 0, 0
    og = ""
    if len(a) > len(b):
        og = b
        new = a
        new += new
        z = len(b)
        fl = True
        while z < len(new):
            if new[y:z] != b:
                # print(y, z, new)
                fl = False
                break
            y = z
            z += len(b)
    else:
        og = a
        new = b
        new += new
        z = len(a)
        fl = True
        while z < len(new):
            if new[y:z] != a:
                # print(y, z, b, new[y:z])
                fl = False
                break
            y = z
            z += len(a)

    val = og
    while len(og) != x:
        og += val

    if fl:
        print(og)
    else:
        print(-1)
