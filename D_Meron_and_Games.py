
import sys, threading

input = lambda: sys.stdin.readline().strip()
from collections import defaultdict, Counter

def main():
    n = int(input())
    arr = list(map(int ,input().split(" ")))
    cp = Counter(arr)
    nums = list(set(arr))
    nums.sort()
    n = len(nums)
    state = defaultdict(int)    
    # print(cp, nums)
    def dp(ind):
        if ind == 0:
            return ind * cp[ind]
            
        if ind == 1:
            return (ind * cp[ind])
        
        if ind in state:
            return state[ind]
        
        res = max(dp(ind-2) + ind * cp[ind], dp(ind-1))

        state[ind] = res
        return res
    print(dp(max(nums)))
    # print(cp, new)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
