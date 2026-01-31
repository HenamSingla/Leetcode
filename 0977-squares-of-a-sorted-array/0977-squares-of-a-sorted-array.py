class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square=[]
        for num in nums:
            x=num**2
            square.append(x)
        new=sorted(square)
        return new