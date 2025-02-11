t = int(input())
from collections import defaultdict, Counter
import bisect
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    cp = Counter(arr)
    ans = [x for x in cp.values()]
    # print(cp)
    ans.sort()
    # print(ans)

    cp = 0
    removed = 0
    prefix = []
    prefix.append(0)
    for ind in range(len(ans)):
        prefix.append(prefix[-1] + ans[ind])
    
    mx = float("inf")
    fin = prefix[-1]
    for ind in range(len(ans)):
        x = bisect.bisect_right(ans, ans[ind])
        bl = bisect.bisect_right(ans, ans[ind]-1)
        left = prefix[bl]


        final_index_of_ind = bisect.bisect_left(ans, ans[ind]+1)
        sum_of_all_elements_after_index = fin - prefix[final_index_of_ind]
        multiplier = ans[ind]* (len(ans) - final_index_of_ind)

        right = abs(sum_of_all_elements_after_index - multiplier)

        mx = min(mx, right + left)

    
    print(mx)
