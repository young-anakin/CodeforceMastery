arr = list(map(int, input().split(" ")))
mx = max(arr)
if mx == 1:
    print("1/1")
elif mx == 6:
    print("1/6")
elif mx == 2:
    print("5/6")
elif mx == 3:
    print("2/3")
elif mx == 4:
    print("1/2")
elif mx == 5:
    print("1/3")