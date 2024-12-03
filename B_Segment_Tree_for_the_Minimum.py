n, m = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
def build_segment_tree(data):
    n = len(data)
    tree = [0] * (2*n)

    for i in range(n):
        tree[n+i] =data[i]
    
    for i in range(n-1, 0, -1):
        tree[i] = min(tree[2*i] , tree[2*i + 1])

    return tree
def update_segment_tree(tree, n, index, value):
     pos = index + n
     tree[pos] = value

     while pos > 1:
         pos //=2
         tree[pos] = min(tree[2*pos] ,  tree[2*pos + 1])


def range_query(tree, n, left, right):
    left += n
    right += n
    sum_val = float("inf")
    while left < right:
        print(left, right)

        if left % 2 == 1:
            # print("fi", tree[left], left)
            sum_val = min(sum_val, tree[left])
            left +=1
        if right %2 == 1:
            right -=1
            sum_val = min(sum_val, tree[right]) 
        
        left //=2
        right //=2
    return sum_val
tree = build_segment_tree(arr)
# print(tree)
# update_segment_tree(tree, n, 1, 8)
for _ in range(m):
    s, i, v = list(map(int, input().split(" ")))

    if s == 1:
        update_segment_tree(tree, n, i, v)
    else:
        print(range_query(tree, n, i, v ))