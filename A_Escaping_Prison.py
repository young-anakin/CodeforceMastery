def numSubarrayProductLessThanK( nums, k):
    prod = 1
    cp = 0
    val = 0

    a = 0
    b = 0

    while b <= len(nums)-1:
        if nums[b] < k:
            val +=1
        prod *= nums[b]
        if prod < k:
            pass

        else:
            temp = b-a
            cp += (temp*(temp+1))//2 - ((b-a))
            prod = int(prod/nums[a])
            a +=1
            print(temp)
        b+=1
        # print(cp, val)
    temp = b-a
    cp += (temp*(temp+1))//2 - ((b-a))
    # print(cp, val)

    return max(0, cp+val)

print(numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3]
, 19
))