class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 0):
            return 0


        minPrice, maxProfit= prices[0], 0

        for price in prices:
            minPrice=min(price, minPrice)
            maxProfit=max(maxProfit, price - minPrice)
        
        return maxProfit