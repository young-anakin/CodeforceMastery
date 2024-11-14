t = int(input())
for _ in range(t):
    l, r, x = list(map(int, input().split(" ")))
    a, b = list(map(int, input().split(" ")))

    if a == b:
        print(0)
    else:

        if a + x > r and a - x < l:
            print(-1)
        elif a < l or b > r:

            print(-1)
        else:
            if l + x > b and r - x < b:

                print(-1)

            elif abs(r-l) < x:

                print(-1)
            else:
                # if (r-a < x and r-b < x) and (l+a < x and l+b < x):
                #     print('d')

                #     print(-1)
                if max(a, b) - min(a,b) >= x:
                    print(1)

                elif (r - a >= x and r- b >= x) or  (l + a >= x and l+b >= x):
                    print(2)

                else:
                    print(3)
                