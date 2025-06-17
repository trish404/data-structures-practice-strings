class Solution(object):
    def frequencySort(self, s):
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        sorted_list = sorted(freq.items(), key = lambda x : -x[1])
        res = ''
        for char, count in sorted_list:
            res += char * count
        return res 
        
