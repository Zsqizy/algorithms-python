#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq > right_sq:
                res[pos] = left_sq
                left += 1
            else:
                res[pos] = right_sq
                right -= 1
            pos -= 1

        return res
               
            
# @lc code=end

