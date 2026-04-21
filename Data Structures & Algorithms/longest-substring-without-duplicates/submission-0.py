class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        _set = set()
        res = 0
        
        for r in range(len(s)):
            while s[r] in _set:
                _set.remove(s[l])
                l += 1 
            
            _set.add(s[r])
            res = max(res, r - l + 1)
        return res