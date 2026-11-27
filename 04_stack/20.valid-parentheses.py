#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for i in s:
            if i in pairs:
                if len(stack)==0 or stack[-1]!=pairs[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack)==0
# @lc code=end

