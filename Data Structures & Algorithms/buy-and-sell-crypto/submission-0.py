class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        l = 0 #buy
        r = 1 #sell
        maxP = 0
        
        while r < len(prices):

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]

                maxP = max(maxP, profit)
            else: 
                l = r

            r = r + 1


        return maxP
        