class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        editedPricesList = prices[1::]
        for idx in range(0,len(editedPricesList)):
            if editedPricesList[idx] > prices[idx]:
                profit += (editedPricesList[idx] - prices[idx]) 
        return profit