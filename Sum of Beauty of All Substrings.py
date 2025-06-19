class Solution(object):
    def beautySum(self, s):
        total = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1

                maxf = 0
                minf = float('inf')

                for count in freq:
                    if count > 0:
                        maxf = max(maxf, count)
                        minf = min(minf, count)

                total += maxf - minf

        return total



        
