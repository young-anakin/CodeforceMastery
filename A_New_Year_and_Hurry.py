def bs(t, fin):
    low = 1
    high = t
    opt = 0

    while low <= high:
        md = (low+high)//2
        # print("Low: ", low, "High: ", high, "Mid: ", md)

        sm = 0
        for ind in range(1,md+1):
            sm += ind * 5
        # print("Sum : ", sm, "Fin : ", fin)
        if sm <= fin:
            opt =  max(md, opt)
            low = md +1
        else:
            high = md -1
    return opt

n, k = list(map(int, input().split(" ")))
remaining = 240 - k
# print("Remaining : ", remaining)
print(bs(n, remaining))
