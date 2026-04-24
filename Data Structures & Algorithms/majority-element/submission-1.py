class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        countMap = {}

        for el in nums:
            if el not in countMap:
                countMap[el] = 1
            else:
                countMap[el] += 1
                
                
        return max(countMap, key=countMap.get)