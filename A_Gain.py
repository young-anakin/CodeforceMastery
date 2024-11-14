def gain():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        b = arr[:]

        arr.sort()
        max_val = arr[-1]
        sec_max_val = arr[-2]

        for i in range(n):
            if b[i] != max_val:
                print(b[i] - max_val, end=' ')
            else:
                print(b[i] - sec_max_val, end=' ')
        
        print()

gain()
