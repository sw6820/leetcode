class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s,m=nums[0],nums[0]
        for i in range(1,len(nums)):
            s=s+nums[i] if nums[i]>nums[i-1] else nums[i]            
            m=max(m,s)    
        return m
                
                
        