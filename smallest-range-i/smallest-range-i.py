class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        t=nums[-1]-nums[0]-2*k
        return t if t>0 else 0