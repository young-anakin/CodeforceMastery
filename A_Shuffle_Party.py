def min_swaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        
        total = 0
        size = ans = len(nums)

#count number of 1’s with a window size of ones

        for idx in range(ones):
            total += nums[idx]
            ans = ones - total
        left = 0

#check the minimum zeros on that window size        
        for right in range(ones , size):
            total -= nums[left]
            total += nums[right]
            left += 1
            ans = min(ans , ones - total)
        
        return ans

# Test cases
data1 = [1,0,1,0,1]
data2 = [0,0,0,1,0]
data3 = [1,0,1,0,1,0,0,1,1,0,1]

print(min_swaps(data1))  # Output: 1
print(min_swaps(data2))  # Output: 0
print(min_swaps(data3))  # Output: 3
