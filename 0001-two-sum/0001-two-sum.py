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




### Neetcode JUNE 5

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[num]=i
            
