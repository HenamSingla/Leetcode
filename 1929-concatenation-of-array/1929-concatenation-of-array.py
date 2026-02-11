# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         #nums=[1,2,3]
#         #ans=[1,2,3,1,2,3]
#         n=len(nums)
#         res=[0]*(2*n)
#         for i in range(n):
#             #i=0,1,2,3,4,5
#                 res[i]=nums[i]
#                 res[i+n]=nums[i]
#         return res
        









class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=nums+nums
        return res