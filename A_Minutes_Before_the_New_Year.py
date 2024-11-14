size = int(input())
for ind in range(size):
    val = list(map(int, input().split(" ")))
    hrs = 23 - val[0]
    mins = 60 - val[1]
    print(60*hrs + mins)
