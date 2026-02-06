class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        #no duplicates
        max_length=0
        num_set=set(nums) #no duplicates O(n)
        print(num_set)

        for num in num_set:
            if num-1 not in num_set:
                length=1
                while num+length in num_set:
                    length+=1
                max_length=max(max_length,length)

        return max_length

        #time: O(3n)~O(n)
        #space: O(n)


    
              
            
