class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1        
        while s<=e:
            m=(s+e)//2
            if target==nums[m]:return m
            elif target<nums[m]: e=m-1                
            else: s=m+1
        return -1
            