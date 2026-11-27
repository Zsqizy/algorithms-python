#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
       ans=[0]*len(temperatures) 
       stack=[]
       for i, temp in enumerate(temperatures):
           while len(stack)!=0 and temp>temperatures(stack[-1]):
               pre=stack.pop()
               ans[pre]=i-pre
       return ans
           
# @lc code=end

