class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                dollar = prices[sell] - prices[buy]
                profit = max(dollar, profit)
            else: 
                buy = sell
            sell += 1
        
        return profit
            