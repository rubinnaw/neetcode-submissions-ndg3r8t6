class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        _set = set(nums)
        res = 0
        
        if not nums:
            return 0
        
        
        for val in _set:
            if val - 1 not in _set:
                cur = val
                lenght = 1
                
                while cur + 1 in _set:
                    cur += 1
                    lenght += 1
                res = max(res, lenght)
        return res