class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ###NEE TO USE A DICTIONARY
        h_map ={}
        for i,num in enumerate(nums):
            comp= target-num
            if comp in h_map.keys():
                return [h_map[comp],i]
            else:
                h_map[num]=i

        