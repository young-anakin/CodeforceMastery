    t = int(input())
    from collections import Counter
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split(" ")))

        cp = Counter(arr)
        ss = set()
        x = 0
        for ind in arr:
            if cp[ind] > 1 and ind not in ss:
                ss.add(ind)
                x +=1

        ans = 0
        for ind in range(len(arr)):
            if cp[arr[ind]] == 1:
                if x == 0:
                    continue
                else:
                    ans +=1
                
            if cp[arr[ind]] > 1:
                cp[arr[ind]] -=1
                ans +=1
                if cp[arr[ind]] == 1: 
                    x -=1
        
        print(ans)