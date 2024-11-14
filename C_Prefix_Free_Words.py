def initialize_trie():
    return {'children': [None, None], 'isLeaf': False, 'isFinished' : False}
 
def insert(curr, word, tot):
    def dfs(curr, word):
        # print(len(word))
        if len(word) == tot:
            curr['isLeaf'] = True
            return word
        
        tmp = None
        fl = True
        if curr['isLeaf'] == False:
            if not curr['children'][0]:
                curr['children'][0] = initialize_trie()
                tmp = dfs(curr['children'][0], word + "0")
                fl = False
            else:
                if not curr['children'][0]['isLeaf']:
                    tmp = dfs(curr['children'][0], word + "0")
                    fl = False
        # if curr['isLeaf']
            if not tmp:
                if not curr['children'][1]:
                    curr['children'][1] = initialize_trie()
                    tmp = dfs(curr['children'][1], word + "1")
                else:
                    if not curr['children'][1]['isLeaf']:
                        tmp = dfs(curr['children'][1], word + "1")
 
        return tmp
    return dfs(curr, word)
 
 
    # current = root
    # for letter in round:
    #     if letter not in current['children']:
    #         current['children'][letter] = initialize_trie()
    #     current = current['children'][letter]
    # current['isLeaf'] = True
 
def search(root, word):
    current = root
    for letter in word:
        if letter not in current['children']:
            return False
        current = current['children'][letter]
    return current['isLeaf']
 
def starts_with(root, prefix):
    current = root
    for letter in prefix:
        if letter not in current['children']:
            return False
        current = current['children'][letter]
    return True
 
# # Example usage:
# trie = initialize_trie()
# insert(trie, "apple")
# insert(trie, "app")
# print(search(trie, "apple"))  # Output: True
# print(search(trie, "app"))    # Output: True
# print(starts_with(trie, "ap")) # Output: True
# print(search(trie, "orange")) # Output: False
 
n = int(input())
arr = list(map(int ,input().split(" ")))
from collections import Counter
cp = Counter(arr)
fl = True
# print(cp)
for ind in range(len(arr)):
    tmp = arr[ind]
    pw = pow(tmp,2)
    if cp[tmp] > pw:
        print("NO")
        fl = False
        break
if fl:
    # print(cp)
    cp[3] = 8
    arr.sort()
    trie = initialize_trie()
    fin = []
    for key, values in cp.items():
        for j in range(values):
            val = (insert(trie, "", key))
            if val != None:
                fin.append(val)
        print(fin)
    # if len(fin) <= n:
    # z    print("YES")

    #     for ind in fin:
    #         print(fin)
    # else:
    #     print("NO")
