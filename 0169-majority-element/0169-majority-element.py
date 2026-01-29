class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #first thought is to use hash map and the max value in the keys is the answer 
        # hashmap={}
        # for num in nums:
        #     if num not in hashmap:
        #         hashmap[num]=1
        #     else:
        #         hashmap[num]+=1
        # print(hashmap)
        # max_value=max(hashmap.values())
        # print(max_value)
        
        # for key,value in hashmap.items():
        #     if value==max_value:
        #         return key
#Time: O(n)
#Space: Hashmap (O(n)) (worst case all diff pairs) 


###Boyer-Moore voting 
        count=0
        res=0
        for num in nums:
            if count==0:
                res=num
            if res==num:
                count+=1
            else:
                count-=1
        return res



