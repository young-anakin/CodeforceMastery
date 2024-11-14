n = int(input())
for ind in range(n):
    a, b = list(map(int, input().split(" ")))
    temp = b//a
    print("temp : ", temp)
    temp = temp + b

    if temp %a == 0:
        print(temp+1)
    else:
        print(temp)