#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count={}
        for ch in s1:
            if ch in s1_count:
                s1_count[ch]+=1
            else:
                s1_count[ch]=1
        w_count={}
        for ch in s2[:len(s1)]:
            if ch in w_count:
                w_count[ch]+=1
            else:
                w_count[ch]=1
        if w_count==s1_count:
            return True
        for right in range(len(s1),len(s2)):
            if s2[right] in w_count:
                w_count[s2[right]]+=1
            else:
                w_count[s2[right]]=1
            left_ch=s2[right-len(s1)]
            w_count[left_ch]-=1
            if w_count[left_ch]==0:
                del w_count[left_ch]
            if w_count==s1_count:
                return True
        return False
            
# @lc code=end

