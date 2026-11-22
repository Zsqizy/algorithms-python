#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_f=0
        max_len=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_f=max(max_f,count[s[right]])
            while (right-left+1)-max_f>k:
                count[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
# @lc code=end

