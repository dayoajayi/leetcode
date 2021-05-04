from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')for _ in range (amount+1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i- coin])
        return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
s = Solution()

print(s.coinChange(coins, amount))

'''
study links:
Algorithm Casts: https://youtu.be/xybIgrSG3qc
Timothy H Chang: https://youtu.be/4S5x4SF4fsM

'''