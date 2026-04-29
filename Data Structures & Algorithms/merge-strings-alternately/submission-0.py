class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = ""
        
        while l <= max(len(word1), len(word2)) - 1:
            if l >= len(word1) and l <= len(word2):
                res += word2[l]
            elif l >= len(word2) and l <= len(word1):
                res += word1[l]
            else:
                res += word1[l]
                res += word2[l]                 
            l += 1
        return res