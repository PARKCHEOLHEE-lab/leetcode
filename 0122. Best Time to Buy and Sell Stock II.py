from typing import List

class Solution:
    """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

        Find and return the maximum profit you can achieve.

        Example 1:
            Input: prices = [7,1,5,3,6,4]
            Output: 7
            Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
            Total profit is 4 + 3 = 7.

        Example 2:
            Input: prices = [1,2,3,4,5]
            Output: 4
            Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
            Total profit is 4.

        Example 3:
            Input: prices = [7,6,4,3,1]
            Output: 0
            Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

        Constraints:
            1 <= prices.length <= 3 * 10^4
            0 <= prices[i] <= 10^4
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1
        
        max_profit = 0
        
        while r < len(prices):
            l_price = prices[l]
            r_price = prices[r]
            
            if l_price < r_price:
                max_profit += r_price - l_price
                
            l = r
            r = l + 1
                
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        for pi in range(len(prices) - 1):
            curr_price = prices[pi]
            next_price = prices[pi + 1]    
            
            max_profit += max(0, next_price - curr_price)
        
        return max_profit

if __name__ == "__main__":
    assert Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit(prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 24
    assert Solution().maxProfit(prices=[1, 2, 1, 2, 1, 3, 5, 1]) == 6