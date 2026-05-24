class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       countmap={}
       for i, n in enumerate(nums):
        difference=target-n
        if difference in countmap:
            return [countmap[difference], i]
        countmap[n]=i