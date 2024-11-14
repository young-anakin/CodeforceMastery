n = int(input())
import heapq
arr = []
ans = []
for _ in range(n):
    a = list(map(str, input().split(" ")))
    if "insert" in a:
        heapq.heappush(arr, int(a[-1]))
        ans.append(" ".join(a))
    elif "removeMin" in a : 
        if arr:
            heapq.heappop(arr)
        else:
            heapq.heappushpop(arr, 0)
            ans.append('insert' + " " + "0")
        ans.append(" ".join(a))
    else:
        target = a[-1]
        while arr and arr[0] < int(target):
            heapq.heappop(arr)
            ans.append("removeMin")
        
        if arr and arr[0] == int(target):
            ans.append('getMin' + target)
        else:
            heapq.heappush(arr, int(target))
            ans.append("insert" + ' ' + target)
            ans.append("getMin" + ' ' + target)
print(len(ans))
for val in ans:
    print(val)