t = int(input())
for _ in range(t):
    c, m, o = list(map(int ,input().split(" ")))
    mn = min(c, m)
    mx = max(c, m)
    available = (mn * 2)
    mx -= mn

    if mx >= mn:
        available += mn
    else:
        available += mx
    
    if o >= mn:
        available += mn
    else:
        available += o
    print(min(available//3, mn*3 // 3))
    # print((mn*2 + min(o, mn) + min(mx-mn, mn))//3)