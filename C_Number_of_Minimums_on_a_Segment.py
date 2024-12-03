n, m = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
import math
def build_segment_tree(data):
    n = len(data)
    tree = [(0, 0)] * (2*n)
    for i in range(n):
        tree[n+i] = (data[i], 1)
    
    for i in range(n-1, 0, -1):
        
        val = min(tree[2*i][0] , tree[2*i + 1][0])
        if tree[2*i][0] > tree[2*i+1][0]:
            cp = tree[2*i+1][1]
        else:
            cp = tree[2*i][1]
        # cp = min(tree[2*i][1], tree[2*i+1])
        if tree[2*i][0] == val and tree[2*i + 1][0] == val:
            cp = (tree[2*i][1] + tree[2*i + 1][1]) 

        tree[i] = (val, cp)

    return tree
def update_segment_tree(tree, n, index, value):
     pos = index + n
    #  print("pos", value)
     if tree[pos][0] != value:
        a, b = tree[pos]
        # if a > value:
        tree[pos] = (value, 1)

        while pos > 1:
            pos //=2
            val = min(tree[2*pos][0] , tree[2*pos + 1][0])
            if tree[2*pos][0] > tree[2*pos+1][0]:
                cp = tree[2*pos+1][1]
            else:
                cp = tree[2*pos][1]
            # cp = min(tree[2*i][1], tree[2*i+1])
            if tree[2*pos][0] == val and tree[2*pos + 1][0] == val:
                cp = (tree[2*pos][1] + tree[2*pos + 1][1]) 

            tree[pos] = (val, cp)
        # print("aaa", tree)
def range_query(tree, n, left, right):
    left += n
    right += n
    sum_val = (float("inf"), 0)
    cp = 0

    while left < right:
        if left % 2 == 1:
            # print("fi", tree[left], left)
            if sum_val[0] > tree[left][0]:
                sum_val = tree[left]
            # sum_val = min(sum_val, tree[left][0])
            left +=1
        if right %2 == 1:
            right -=1
            if sum_val[0] > tree[right][0]:
                sum_val = tree[right]
            # sum_val = min(sum_val, tree[right][0]) 
        
        left //=2
        right //=2
    return sum_val
tree = build_segment_tree(arr)
print(tree)
# update_segment_tree(tree, n, 1, 8)
for _ in range(m):
    s, i, v = list(map(int, input().split(" ")))

    if s == 1:
        update_segment_tree(tree, n, i, v)
    else:
        # pass
        # print('da')
        print(range_query(tree, n, i, v ))