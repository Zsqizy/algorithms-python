#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+' or i=='-' or i=='*' or i=='/':
                a=stack.pop()
                b=stack.pop()
                if i=='+':
                    stack.append(b+a)
                elif i=='-':
                    stack.append(b-a)
                elif i=='*':
                    stack.append(b*a)
                elif i=='/':
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]
# @lc code=end

