def initialize_trie():
    return {'children': {}, 'isLeaf': False}

def insert(root, word):
    current = root
    for letter in word:
        if letter not in current['children']:
            current['children'][letter] = initialize_trie()
        current = current['children'][letter]
    current['isLeaf'] = True

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

# Example usage:
trie = initialize_trie()
insert(trie, "apple")
insert(trie, "app")
print(search(trie, "apple"))  # Output: True
print(search(trie, "app"))    # Output: True
print(starts_with(trie, "ap")) # Output: True
print(search(trie, "orange")) # Output: False
