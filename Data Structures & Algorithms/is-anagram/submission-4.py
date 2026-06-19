class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k={}
        h={}
        if len(s)!=len(t):
            return False
        for char in s:
            if s in k:
                k[char]+=1
            else:
                k[char]=1
        for char in t:
            if t in h:
                h[char]+=1
            else:
                h[char]=1
        if k==h:
            return True
        else:
            return False
        
        
        