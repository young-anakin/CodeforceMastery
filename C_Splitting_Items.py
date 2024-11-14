t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    arr.sort(reverse=True)
    alice = 0
    bob = 0
    turn = True
    # print(arr)
    for ind in range(len(arr)):
        if turn:
            alice += arr[ind]
            turn = False
        else:
            turn = True
            sub = abs(arr[ind-1] - arr[ind])
            # print(k, sub)
            if k >= sub:
                bob += arr[ind] + sub
                # print(arr[ind], sub)
                k -= sub
            else:
                bob += arr[ind] + k
                # print(bob, arr[ind], k)
                k = 0
    print(abs(bob-alice))