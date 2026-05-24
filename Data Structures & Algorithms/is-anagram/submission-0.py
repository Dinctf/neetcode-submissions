class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countmap={}
        for char in s:
            if char not in countmap:
                countmap[char]=1
            else:
                countmap[char]+=1
        count={}
        for char in t:
            if char not in count:
                count[char]=1
            else:
                count[char]+=1
        if countmap==count:
            return True
        else:
            return False