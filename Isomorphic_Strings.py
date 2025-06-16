class Solution(object):
    def isIsomorphic(self, s, t):
        def encode(word):
            mapping = {}
            code = []
            idx = 0
            for ch in word:
                if ch not in mapping :
                    mapping[ch] = idx
                    idx +=1
                code.append(mapping[ch])
            return code 
        return encode(s) == encode(t) 



        
