class Solution(object):
    def maxDepth(self, s):
        currd = 0
        maxd = 0
        for char in s:
            if char == '(':
                currd += 1
                maxd = max(currd, maxd)
            elif char == ')':
                currd -= 1
        return maxd
        
