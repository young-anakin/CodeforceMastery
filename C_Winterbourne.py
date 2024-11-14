n = int(input())
for a in range(n):
    arr = list(map(int, input().split(" ")))
    seats = list(map(int, input().split(" ")))
    if arr[1] < arr[0]:
        print("NO")
    else:
        seats.sort()
        seats.reverse()
        # print(seats)
        summ = 0
        for a in range(arr[0]):
            if a == 0:
                summ += (2 * seats[a]) + 1
            elif a == arr[0]-1:
                summ += 1
            else:
                summ += seats[a] + 1
        if summ <= arr[1]:
            print("YES")
        else:
            print("NO")
