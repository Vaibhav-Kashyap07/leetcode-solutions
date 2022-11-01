class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) + 1
        return set(range(n)).difference(set(nums)).pop()