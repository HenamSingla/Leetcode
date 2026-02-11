class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #nums=[1,2,3]
        #ans=[1,2,3,1,2,3]
        n=len(nums)
        res=[0]*(2*n)
        for i in range(len(nums)):
            #i=0,1,2,3,4,5
                res[i]=nums[i]
                res[i+n]=nums[i]
        return res
        

