class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        current_profit = 0
        
        for price in prices:
            min_price = min(price,min_price)
            profit = price - min_price
            current_profit = max(current_profit, profit)
            
        return current_profit
            
        