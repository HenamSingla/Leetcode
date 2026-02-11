class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        for i,num in enumerate(nums):
            for j,num in enumerate(nums):
                if nums[i]>nums[j] and j!=i:
                    res[i]+=1
                
        return res


