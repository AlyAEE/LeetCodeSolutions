class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#Constraints
# you want to return the maximum profit possible
# you must sell after you buy
#Considerations
# 1. is this the cheapest price i got
# 2. if i subtract the current price by the cheapest price, do i get the maximum profit

        cheapest_price = float('inf')
        maximum_profit = 0
        for i in prices:
            if i < cheapest_price:
                cheapest_price = i
            profit = i - cheapest_price
            if profit > maximum_profit :
                maximum_profit = profit
        return maximum_profit
# This solves the problem in a time complexity O(n) and space complexity O(1)