def merge(left_half,right_half):
    # write your code here
    new_arr = []
    l = 0
    r = 0
    while l <= len(left_half)-1 and r <= len(right_half)-1:
        if left_half[l] <= right_half[r]:
            new_arr.append(left_half[l])
            l+=1
        else:
            new_arr.append(right_half[r])
            r +=1
        
        if len(right_half) != 0:
            new_arr.extend(right_half)
        if len(left_half) != 0:
            new_arr.extend(left_half)
        return new_arr
def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
   
    return merge(left_half, right_half)

def test():
    print(mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10])
    # assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    # assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    # print("Great Job !!!")
test()
