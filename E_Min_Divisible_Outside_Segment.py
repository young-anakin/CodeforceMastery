t = int(input())
for _ in range(t):
    l, r ,n = list(map(int, input().split(" ")))
    og = n
    og_r = r
    if n < l:
        print(n)
    elif n > r:
        print(n)
    else:
        while n <= r:
            n *=2
        print(n)
        ab = float("inf")
        # print(r, n)
        mn = n
        md = (r + n)//2
        # print(mn)
        # print(n, r)
        # print(mn, md)
        while n > r:
            md = (n+r)//2
            if md % og == 0 and md != r:
                mn = min(mn, md)
            else:
                if md - (md%og) < r or md - (md%og) == og_r:
                    # print(111, md - (md%og))
                    pass
                else:
                    # print(112, md - (md%og), n, og_r)

                    mn = min(mn, md- (md%og))
            # print(md)

            n = md
        print(mn)


        # while mn > r:
