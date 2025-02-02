n = int(input())
volume = list(map(int, input().split(" ")))
capacity = list(map(int, input().split(" ")))

sm = sum(volume)
capacity.sort()
a, b = capacity[-1], capacity[-2]

if sm <= a +b:
    print("YES")
else:
    print("NO")