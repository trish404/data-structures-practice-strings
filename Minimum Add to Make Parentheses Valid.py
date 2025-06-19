class Solution(object):
    def minAddToMakeValid(self, s):
        opencount = 0
        addtobal = 0

        for ch in s:
            if ch == '(':
                opencount += 1
            elif ch == ')':
                if opencount > 0:
                    opencount -= 1
                else:
                    addtobal += 1
        
        return opencount + addtobal 
            
        
