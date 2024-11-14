
import sys, threading

input = lambda: sys.stdin.readline().strip()
from collections import defaultdict, Counter, deque

def main():
    t = int(input())

    for _ in range(t):
        dir = [(0,1), (1, 0)]
        n, m , k = list(map(int, input().split(" ")))
        def inbound(i, j):
            return i >= 0 and j >= 0 and i <= n and j <= m

        the_grid = [[0 for _ in range(m)] for _ in range(n)]
        
        for ind in range(n):
            for j in range(m):
                if j == 0:
                    the_grid[ind][j] = ind
                    continue
                the_grid[ind][j] += the_grid[ind][j-1] + ind+1
        if the_grid[-1][-1] == k:
            print("YES")
        else:
            print("NO")
        # return "YES" if the_grid[-1][-1] == k else "NO"
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
