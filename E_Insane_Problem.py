from math import ceil

def generatePowers(base):
    value = base
    powers = []

    while value < 1000000001:
        powers.append(value)
        value *= base
    
    return powers

def processTestCase():
    # Directly read the input
    base, lower1, upper1, lower2, upper2 = map(int, input().strip().split())
    
    powers = generatePowers(base)
    validCount = 0
    for power in powers:
        lowerBound = max(lower1, ceil(lower2 / power))
        upperBound = min(upper1, upper2 // power)
        
        validCount += max(0, upperBound - lowerBound + 1)
       
    overlapCount = max(0, min(upper1, upper2) - max(lower1, lower2) + 1)
    print(validCount + overlapCount)

# Read the number of test cases
testCases = int(input().strip())
for _ in range(testCases):
    processTestCase()
