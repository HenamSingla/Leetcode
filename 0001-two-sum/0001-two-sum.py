class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for num in nums:
        #     remaining = target - num
        #     if remaining in nums and nums.index(num) != nums.index(remaining):
        #         return [nums.index(num), nums.index(remaining)]
        
        
        dictionary = {}
        if len(nums) == 2:
            return[0,1]
        for i, num in enumerate(nums):
            remain = target - num
            if num in dictionary.keys() and i != dictionary[num]:
                return[i,dictionary[num]]

            dictionary[remain] = i
            # print(i)
            # print(dictionary)

            
            
                