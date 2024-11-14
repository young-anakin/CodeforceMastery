t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    odd, even = 0,0
    for ind in arr:
        if ind%2 == 0:
            even +=1
        else:
            odd +=1
    # print(odd, even)

    if x == 1 and odd >=1:
        print("Yes")
    elif x == 1 and odd == 0:
        print("No")
    elif x == 3:
        if odd >= 3 or (even >= 2 and odd >= 1):
            print("Yes")
        else:
            print("No")
    elif x%2 == 1:
        tot = x-1
        # print(odd, even, tot)
        if odd >= (tot)//2 and even >= (tot)//2:
            odd -=tot//2
            even -=tot//2
            # print(even, odd)
            if odd <= 0:
                print("No")
            else:
                print("Yes")
        else:
            print("No")
    else:
        # print(odd, even, x//2)
        if (odd) >= (x//2) and (even) >= (x//2):
            print("Yes")
        else:
            print("No")