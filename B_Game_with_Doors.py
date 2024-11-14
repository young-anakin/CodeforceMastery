t = int(input())
for _ in range(t):
    alice = list(map(int, input().split(" ")))
    bob = list(map(int, input().split(" ")))
    alice.sort()
    bob.sort()
    arr = []
    if alice[0] == bob[0] and alice[1] == bob[1]:
        print(abs(alice[0] - bob[1]))
    elif max(alice)+1 ==  min(bob) or max(bob)+1 == min(alice):
        print(1)
    elif max(alice) <  min(bob) or max(bob) < min(alice):
        print(1)
    else:
        arr.extend(bob)
        arr.extend(alice)
        arr.sort()
        cp = 0
        cp += abs(arr[1] -arr[2])
        if arr[0] != arr[1]:
            cp +=1
        if arr[2] != arr[3]:
            cp +=1
        # print(arr)
        print(cp)
    
