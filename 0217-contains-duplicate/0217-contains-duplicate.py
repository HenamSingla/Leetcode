class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and i!=j:
        #             return True 
        # return False

        ###NEED TO USE SET
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False