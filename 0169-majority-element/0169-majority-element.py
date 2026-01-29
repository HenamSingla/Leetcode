class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #first thought is to use hash map and the max value in the keys is the answer 
        hashmap={}
        for i,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        print(hashmap)
        max_value=max(hashmap.values())
        print(max_value)
        
        for key,value in hashmap.items():
            if value==max_value:
                return key
