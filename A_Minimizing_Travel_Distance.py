li = list(map(int, input().split(" ")))

li.sort()

print(li[1] - li[0] + li[2] - li[1])