player1, player2 = list(map(int, input().split(" ")))
from collections import defaultdict
memo = defaultdict(int)
def dp(player1, player2):
    if player1 < 0 or player2 < 0:
        return -1
    if player1 <= 0 or player2 <= 0:
        return 0
    if not memo:
        x = max(dp(player2-2, player1+1) + 1, dp(player1-2, player2+1)+1)
        memo[(player1, player2)] = x
    
    return memo[(player1, player2)]

dp(player1, player2)
print(memo[player1, player2])