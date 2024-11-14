from collections import Counter
def check(val):
    start = 0
    nums = [10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111, 100000]
    cp = Counter(str(val))
 
    if len(cp) == 1 and (cp['1'] >= 1 or cp['0'] >= 1):
        return ("YES")
 
 
    elif len(cp) == 2 and ( cp['1'] >=1 and cp['0'] >=1):
        return ("YES")
    
    while start < len(nums):
        while val % nums[start] == 0:
            val = val //nums[start]
        start += 1
    
    if val == 1:
        return('YES')
    else:
        return('NO')
    
    
t = int(input())
for ind in range(t):
    val = input()
    print(check(int(val)))