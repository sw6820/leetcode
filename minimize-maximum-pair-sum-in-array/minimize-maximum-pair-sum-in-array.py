class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m,l=0,len(nums)
        for i,v in enumerate(nums[:l//2]):m=max(m,v+nums[l-1-i])            
        return m
        