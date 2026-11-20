#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts={}
        for num in nums:
            counts[num]=counts.get(num,0)+1
        counts=counts.items()
        counts=sorted(counts,key=lambda  x: x[1], reverse=True)
        ans=[]
        for pair in counts[:k]:
            ans.append(pair[0])
        return ans
# @lc code=end

