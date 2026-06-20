class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        sorted_pair=sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_pair[i][0])
        return ans