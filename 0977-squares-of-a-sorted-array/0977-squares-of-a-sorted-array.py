class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square=[]
        for num in nums:
            x=num**2
            square.append(x)
        #uses timesort
        new=sorted(square)
        return new

#time: O(nlogn)
#space:O(n)

