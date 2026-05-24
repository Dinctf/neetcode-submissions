class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap={}
        for num in nums:
            if num in countmap:
                countmap[num]+=1
                return True
            else:
                countmap[num]=1
        return False