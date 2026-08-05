class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maxP = 0
        r = 1

        while r < len(prices):

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            else:
                l = r

            r = r + 1

        return maxP

            

        