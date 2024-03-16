from typing import List

class Solution:
    """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Example 1:
            Input: prices = [7,1,5,3,6,4]
            Output: 5
            Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                         Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
            
        Example 2:
            Input: prices = [7,6,4,3,1]
            Output: 0
            Explanation: In this case, no transactions are done and the max profit = 0.

        Constraints:
            1 <= prices.length <= 10^5
            0 <= prices[i] <= 10^4
    """
    
    # Time Limit Exceeded
    def maxProfitNaive(self, prices: List[int]) -> int:
        
        max_profit = 0
        for ppi, prev_price in enumerate(prices):
            for next_price in prices[ppi + 1:]:
                if prev_price < next_price:
                    max_profit = max(max_profit, next_price - prev_price)        
        
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        
        li = 0
        ri = li + 1
        
        max_profit = 0
        
        while ri < len(prices):
            l_price = prices[li]
            r_price = prices[ri]
            
            if l_price < r_price:
                max_profit = max(max_profit, r_price - l_price)
                ri += 1
                
            elif l_price > r_price:
                l_price = r_price
                li = ri
                ri = li + 1
                
            else:
                ri += 1        
        
        return max_profit
    

if __name__ == "__main__":
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
    print(Solution().maxProfit(prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))
    print(Solution().maxProfit(prices=[1, 2, 1, 2, 1, 3, 5, 1]))