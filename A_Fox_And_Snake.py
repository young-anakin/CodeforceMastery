n, m = list(map(int, input().split(" ")))
stub = []
for ind in range(n):
    arr = []
    turn = True
    if ind%2 == 0:
        for j in range(m):
            arr.append("#")
    else:
        for j in range(m):
            arr.append('.')
        turn = not(turn)
    stub.append(arr)
turn = True
a = 1
while a <= len(stub)-1:
    if turn:
        stub[a][-1] = "#"
        turn = False
    else:
        stub[a][0] = "#"
        turn = True
    a +=2
for ind in range(len(stub)):
    print("".join(stub[ind]))