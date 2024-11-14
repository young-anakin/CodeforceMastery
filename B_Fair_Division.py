t = int(input())
for _ in range(t):
    sz = int(input())
    arr = list(map(int, input().split(" ")))

    sm = sum(arr)//2
    if arr.count(1) %2 != 0:
        print("NO")
        continue
    if arr.count(1) == 0 and arr.count(2)%2 != 0:
        print("NO")
        continue
    from collections import defaultdict
    memo = defaultdict(int)
    def dp(ind, tar):
        if ind == sz:
            return tar == 0
        
        if tar == 0:
            return True

        if (ind, tar) not in memo:
             memo[(ind, tar)] = dp(ind+1, tar - arr[ind]) or dp(ind+1, tar)

        return memo[(ind, tar)]

    if dp(0, sm):
        print("YES")
    else:
        print("NO")