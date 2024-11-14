t = int(input())
for _ in range(t):
    val = int(input())
    arr = [i for i in range(1, val+1)]
    if val %2 == 0:

        print(* arr[::-1])
    else:
        arr[val//2], arr[(val//2) + 1] = arr[(val//2) + 1], arr[val//2]
        print(* arr[::-1])
