class Solution(object):
    def isAnagram(self, s, t):
        def encode(str):
            enc = {}
            for ch in str:
                if ch in enc:
                    enc[ch] += 1
                else:
                    enc[ch] = 0
            return enc
        x = encode(s)
        y = encode(t)
        if x == y:
            return True 
        else:
            return False
