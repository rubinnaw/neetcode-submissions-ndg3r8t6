class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        l, r = 0, k - 1
        nums.sort()
        res = float("inf")
        
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res