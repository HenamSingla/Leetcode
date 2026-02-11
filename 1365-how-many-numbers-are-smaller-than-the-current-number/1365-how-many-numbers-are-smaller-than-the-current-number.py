class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # res=[0]*n
        # for i in range(n):
        #     for j in range(n):
        #         if nums[i]>nums[j] and j!=i:
        #             res[i]+=1
                
        # return res
        n=len(nums)
        res=[0]*n
        sort_nums=sorted(nums)
        print(sort_nums)
        for i,num in enumerate(nums):
            pos=sort_nums.index(num)
            res[i]=pos
        return res