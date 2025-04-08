class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        freq=[]
        for i in range(len(nums)+1):
            freq.append([])
        for num in count:
            frequency=count[num]
            freq[frequency].append(num)
        
        res=[]
        i=len(freq)-1
        while i>=0:
            for num in freq[i]:
                res.append(num)
            if len(res)==k:
                return res
            i-=1
        return res