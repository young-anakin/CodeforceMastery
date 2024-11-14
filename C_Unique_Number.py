t = int(input())
for _ in range(t):
    n = int(input())
    sm = (9 * 8)/2
    arr = [1,2,3,4,5,6,7,8,9]
    if n > 45:
        print(-1)
    else:
        ans = ""
        mx = 9
        sm = 0
        while sm != n:
            needed = n - sm
            if needed in arr:
                ans += str(needed)
                break
            sm += arr[-1]
            ans += str(arr.pop())
        
        ans = ans[::-1]
        print(ans)