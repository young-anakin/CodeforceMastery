n, a, b, c = list(map(int, input().split(" ")))
arr = [a,b,c]
import sys, threading

input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
def main():
    memo = defaultdict(int)
    def dp(ind, sm, rib):
        if sm == 0:
            return rib
        if sm < 0:
            return 0
        
        if (ind, sm) not in memo:
            memo[(ind, sm)] = max(dp(a, sm - a , rib+1), dp(b, sm -b, rib+1), dp(c, sm - c,rib+1 ))

        return memo[(ind, sm)]
    arr.sort()
    a, b, c = arr[0], arr[1], arr[2]
    # print(arr)

    mx = max(dp(a, n, 0), dp(b, n, 0), dp(c, n, 0))
    print(mx)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
