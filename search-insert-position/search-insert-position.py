class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        while s<e:
            m=(s+e)//2
            if target<nums[m]: e=m
            elif target>nums[m]: s=m+1
            else: return m
        return e+1 if target>nums[e] else e        