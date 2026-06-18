class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        k={}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in h:
                h[ch]+=1
            else:
                h[ch]=1
        for ch in t:
            if ch in k:
                k[ch]+=1
            else:
                k[ch]=1
        if h==k:
            return True
        else:
            return False
        