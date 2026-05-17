class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        i=1
        max_profit=0
        while i<len(prices):
            if prices[l]<prices[i]:
                price_d=prices[i]-prices[l]
                max_profit=max(max_profit,price_d)
                
            else:
                l=i
            i+=1
        return max_profit
                
            
        