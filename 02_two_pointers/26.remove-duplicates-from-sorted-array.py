#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       slow=1
       for fast in range(1,len(nums)):
           if nums [fast]!=nums[fast-1]:
               nums[slow]=nums[fast]
               slow+=1
       return slow
# @lc code=end


