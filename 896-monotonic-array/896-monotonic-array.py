class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        f=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                if f in (0,1):
                    f=1
                else: return False
            elif nums[i-1]>nums[i] :
                if f in (0,-1):
                    f=-1
                else: return False
        return True