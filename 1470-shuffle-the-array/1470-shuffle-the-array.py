# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
        # res=[0]*(2*n)
        # for i in range(n):
        #     #0,1,2
        #     res[2*i]=nums[i]
        #     #res[0,2,4]
        #     res[2*i+1]=nums[n+i]
        #     #res[1,3,5]
        # return res










class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        res=[]
        while i<n:
            res.append(nums[i])
            res.append(nums[i+n])
            i+=1
        return res