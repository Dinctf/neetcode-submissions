class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        k={}
        l={}
        for char in s:
            if char in k:
                k[char]+=1
            else:
                k[char]=1
        for char in t:
            if char in l:
                l[char]+=1
            else:
                l[char]=1
        if k==l:
            return True 
        else:
            return False
            
        