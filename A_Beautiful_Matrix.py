def Solution(ans):
    # print(ans)
    return abs(3-ans[0]) + abs(3 - ans[1])



ans = []
for i in range(1, 6):
    arr = list(map(int, input().split(" ")))
    if 1 in arr:
        ans.append(i)
        ans.append(arr.index(1)+1)
        break
    arr = []
    
print(Solution(ans))
