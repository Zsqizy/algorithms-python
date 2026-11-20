#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups={}
        for word in strs:
            key="".join(sorted(word))
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())

# @lc code=end

