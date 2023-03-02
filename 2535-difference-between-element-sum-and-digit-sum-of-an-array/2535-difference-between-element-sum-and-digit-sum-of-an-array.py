class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:        
        return abs(sum([sum(map(int,[*str(n)])) for n in nums])-sum(nums))