class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        x=nums.index(m)  
        if len(nums)==1: return 0
        return -1 if m <2*sorted(nums)[-2] else x