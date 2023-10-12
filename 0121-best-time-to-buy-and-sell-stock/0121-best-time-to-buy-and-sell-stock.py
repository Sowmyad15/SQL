class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        max_profit=0
        while r<len(prices):
            curr_profit=prices[r]-prices[l]
            if curr_profit>0:
                max_profit=max(max_profit,curr_profit)
            else:
                l=r
            r=r+1
        return max_profit

        