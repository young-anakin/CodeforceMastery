import sys
from math import gcd
 
def solve():
	# Read input for the number of elements, string, and array of integers
	n = int(sys.stdin.readline().strip())
	s = sys.stdin.readline().strip()
	a = list(map(int, sys.stdin.readline().split()))
 
	lcm = 1
	vis = [0] * n
	for i in range(n):
        if vis[i]:
        	continue
    	cur = []
    	ind = i
    	# Traverse the cycle starting from current index
    	while not vis[ind]:
        	cur.append(s[ind])
        	vis[ind] = 1
        		ind = a[ind] - 1
    	# Create a search string by repeating current cycle twice
    	search = "".join(cur + cur)
    	# Remove the first character (repetition), if we dont remove it the answer will always be 0
    	search = search[1:]  
    	# Find the starting index of the cycle
    	index = search.find("".join(cur)) + 1  
    	lcm = (lcm* index) // gcd(lcm, index)
	return lcm
 
if __name__ == "__main__":
 
	t = int(sys.stdin.readline().strip())
	for _ in range(t):
    	# Call solve() for each test case and print the result
    	result = solve()
    	print(result)