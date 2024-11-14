
t = int(input())
for ind in range(t):
    sz = int(input())
    arr = list(map(int, input().split(" ")))
    ps = [0]
    for j in range(len(arr)):
        ps.append(ps[-1] + arr[j])
    
    n = int(input())
    final = []

    for ind in range(n):
        a, u = list(map(int, input().split(" ")))

        l = a
        r = sz
        mn = -float("inf")

        tot = u
        while l <= r:
            md = (l+r)//2
            ans = ps[md] - ps[a-1]
            first = (u * (u+1))//2
            ux = u - (ans)
            second = (ux * (ux+1))//2
            first -= second
            if first == mn:
                tot = min(tot, md)
            elif first > mn:
                mn = first
                tot = md
            if u - (ans-1) > 0:
                l = md+1
            else:
                r = md - 1
        
        final.append(tot) 
    print(" ".join(map(str, final)))
