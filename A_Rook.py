let = "abcdefgh"
num = "12345678"

n = int(input())
for ind in range(n):
    x = input()
    for ind in range(8):
        if x[0] + num[ind] != x:
            print(x[0] + num[ind])

        if let[ind] + x[1] != x:
            print(let[ind] + x[1])