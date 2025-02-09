t = int(input())
from collections import defaultdict
for _ in range(t):
    n, q = list(map(int, input().split(" ")))
    arr = input()

    def dp(sub, ans):
        if len(sub) == len(ans):
            if sub == ans:
                return True
            else:
                return False
        


    for _ in range(q):
        a, b = list(map(int, input().split(" ")))

        sub = arr[a-1:b]

        # print(sub)
        if sub[0] in arr[0:a-1] or sub[-1] in arr[b:]:
            print("YES")
        else:
            print("NO")