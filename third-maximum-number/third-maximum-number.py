class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)),reverse=True)                                
        return nums[0] if len(nums)<3 else nums[2]