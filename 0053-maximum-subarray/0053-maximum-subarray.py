class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=[nums[0]]
        m=nums[0]
        for i in range(1,len(nums)):
            s.append(max(s[-1],0)+nums[i])
            m=max(m,s[-1])
        return m