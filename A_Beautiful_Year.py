n = input()
arr = list(map(int, input().split(' ')))
if arr.count(1) >= 1:
    print("HARD")
else:
    print("EASY")