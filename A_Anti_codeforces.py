
# Here's the Python code to solve the Palindrome Formation problem:

# Python
def can_form_palindrome(s):
    """
    Determines if a string can be made a palindrome using Inversion Magic once.

    Args:
        s: The binary string.

    Returns:
        True if it's possible to form a palindrome, False otherwise.
    """

    n = len(s)
    differences = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            differences += 1
            if differences > 2:
                return False

    return differences <= 1  # Allow at most one difference or zero differences

# Test cases
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    result = "Yes" if can_form_palindrome(s) else "No"
    print(result)