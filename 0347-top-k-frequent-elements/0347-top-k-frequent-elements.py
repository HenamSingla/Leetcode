# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         unique =[]
#         nums.sort()
#         for num in nums:
#             if num not in unique:
#                 unique.append(num)
        
#         return unique[:k]

#         count = Counter(nums)

#         # Sort the count dictionary by frequency and get the keys
#         # The sorted function returns a list of tuples (key, value) sorted by value (frequency)
#         sorted_keys = sorted(count, key=count.get, reverse=True)

#         # Return the first k elements from the sorted keys
#         return sorted_keys[:k]

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # unique =[]
        # nums.sort()
        # for num in nums:
        #     if num not in unique:
        #         unique.append[num]
        
        # return unique
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


    
    
    