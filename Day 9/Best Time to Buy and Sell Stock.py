class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        max_profit=0
        for i in prices:
            if i<=minimum:
                minimum=i
            else:
                max_profit=max(i-minimum,max_profit)
        return max_profit
