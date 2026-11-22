#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
       left=0
       max_profit=0
       for right in range(len(prices)):
           if prices[right]>prices[left]:
               max_profit=max(max_profit,prices[right]-prices[left]) 
           else:
               left=right
       return max_profit
# @lc code=end

