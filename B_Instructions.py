
import sys, threading

input = lambda: sys.stdin.readline().strip()
from collections import defaultdict

def main():
    t = int(input())
    for _ in range(t):
        memo = defaultdict(int)

        n = int(input())
        arr = list(map(int, input().split(" ")))

        def dp(ind):
            if ind >= n:
                # print("fin", ind)
                return 0
            

            if (ind) not in memo:
                # sm += arr[ind]
                # print(arr[ind], sm)
                memo[ind] = arr[ind] + dp(ind + arr[ind])

            return memo[ind]
        mx = 0
        for ind in range(n):
            mx = max(dp(ind), mx)
        print(mx)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
