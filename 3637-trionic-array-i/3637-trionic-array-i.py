from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1) strictly increasing: nums[0..p]
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        p = i
        if p == 0 or p == n - 1:
            return False  # need room before and after p

        # 2) strictly decreasing: nums[p..q]
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        q = i
        if q == p or q == n - 1:
            return False  # must decrease at least once and leave room for final increase

        # 3) strictly increasing: nums[q..n-1]
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
