from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, 1000000 # float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


prices = [7,1,5,3,6,4]    # ==> 5
# prices = [7,6,4,3,1]      # ==> 0
#prices = []                # ==> 0

s = Solution()

print(s.maxProfit(prices))