#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        wsum=sum(nums[:k])
        msum=wsum
        for right in range(k,len(nums)):
            wsum=wsum+nums[right]-nums[right-k]
            msum=max(msum,wsum)
        return msum/k
# @lc code=end

