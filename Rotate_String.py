class Solution(object):
    def rotateString(self, s, goal):
        flag = False
        if len(s) != len(goal):
            return False
        x = len(s) -1
        while x >= 0:
            if s == goal:
                flag = True
            s = s[1:]+s[0]
            x -= 1 
        return flag
        
