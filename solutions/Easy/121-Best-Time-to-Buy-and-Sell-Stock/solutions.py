class Solution:
    def maxProfit(self, prices: List[int]) 
-> int:
        if len(prices) == 0:
            return 0
        lowestPrice = prices[0]
        currProfit = 0
        index = 1
        while index < len(prices):
            if prices[index] <= lowestPrice:
                lowestPrice = prices[index]
            else:
                currProfit = max(currProfit, 
prices[index]-lowestPrice)
            index+=1
        return currProfit