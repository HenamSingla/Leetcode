class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count=0
        # for num in nums:
        #     while num==1:
        #         count+=1
        #     print(count)
        # return count
        current_sum=0
        max_sum=0
        for num in nums:
            if num==1:
                current_sum+=1
            else:
                current_sum=0
            max_sum=max(max_sum,current_sum)
        return max_sum
            


        