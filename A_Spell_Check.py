from collections import defaultdict
n = int(input())
check = {"T": 1, "i": 1, "m": 1, "u":1, "r":1}
for ind in range(n):
    x = int(input())
    val = input()
    dict = defaultdict(int)
    for j in range(len(val)):
        dict[val[j]] +=1
    if dict != check:
        print("NO")
    else:
        print("YES")