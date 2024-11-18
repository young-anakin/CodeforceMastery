import heapq

def solve_case(n, m, l, hurdles, power):
    pq = []
    
    currentPower = 1
    took = 0
    i, j = 0, 0
    can = True
    
    while i < n:
        while j < m and hurdles[i][0] > power[j][0]:
            heapq.heappush(pq, -power[j][1])
            j += 1
            
        
        req = hurdles[i][1] - hurdles[i][0] + 2
        
        while pq and currentPower < req:
            took += 1
            currentPower += -heapq.heappop(pq)
        
        if currentPower < req:
            can = False
            break
        
        i += 1
    
    if not can:
        return -1
    else:
        return took

def main():
    t = int(input())
    for _ in range(t):
        n, m, l = map(int, input().split())
        hurdles = [tuple(map(int, input().split())) for _ in range(n)]
        power = [tuple(map(int, input().split())) for _ in range(m)]
        print("Hurdles", hurdles)
        print("Power", power)
        result = solve_case(n, m, l, hurdles, power)
        print(result)

if __name__ == "__main__":
    main()
