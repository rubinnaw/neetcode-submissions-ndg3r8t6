class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = []
        
        while l <= max(len(word1), len(word2)) - 1:
            if l >= len(word1) and l <= len(word2):
                res.append(word2[l])
            elif l >= len(word2) and l <= len(word1):
                res.append(word1[l])
            else:
                res.append(word1[l])
                res.append(word2[l])
            l += 1
            
        return "".join(res)