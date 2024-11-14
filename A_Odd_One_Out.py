n = int(input())
i = 0
while i < n: 
    li = list(map(int, input().split(" ")))

    if li[0] == li[1]:
        print(li[2])
    elif li[1] == li[2]:
        print(li[0])
    else:
        print(li[1])



    i+=1
