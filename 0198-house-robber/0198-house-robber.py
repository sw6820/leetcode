class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        s=[0]*l
        s[0]=nums[0]
        if l>1: s[1]=max(nums[0],nums[1])
        for i in range(2,l):
            s[i]=max(s[i-1],s[i-2]+nums[i])        
        return s[-1]
            
            