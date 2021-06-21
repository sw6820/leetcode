class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        m=0
        nums.sort()
        for i in range(len(nums)):
            if i: m=max(m, nums[i]-nums[i-1])            
        return m