t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n %2 == 0:
        print(-1)
    else:
        arr = [i for i in range(1, n+1)]
        fin = arr[0:n//2+1][::-1] + arr[n//2+1:]
        print(*fin)