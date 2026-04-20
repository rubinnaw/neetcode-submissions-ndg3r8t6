class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxVal = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxVal = max(maxVal, profit)
            else:
                l = r
            r += 1
        return maxVal