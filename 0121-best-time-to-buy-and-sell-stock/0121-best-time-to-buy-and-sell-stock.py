class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=float('inf')
        
        for p in prices:
            if p<buy:
                buy=p
            current_profit=p-buy
            # print(buy)
            # print(current_profit)
            profit=max(profit,current_profit)
        return profit

        #time: O(n)
        #space: O(1)
        


                    