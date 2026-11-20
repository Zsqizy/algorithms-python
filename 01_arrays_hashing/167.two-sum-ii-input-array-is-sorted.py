#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            sums=numbers[left]+numbers[right]
            if sums==target:
                return [left+1,right+1]
            elif sums<target:
                left+=1
            else:
                right-=1
        return []
# @lc code=end

