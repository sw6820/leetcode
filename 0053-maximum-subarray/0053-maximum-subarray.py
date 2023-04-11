class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        D,M=nums[0],nums[0]        
        for i in range(1,len(nums)):
            D=max(D,0)+nums[i]
            M=max(M,D)
        return M