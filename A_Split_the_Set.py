t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    odd, even = 0,0
    for val in arr:
        if val%2 == 0:
            even +=1
        else:
            odd +=1
    if odd == even:
        print("Yes")
    else:
        print("No")