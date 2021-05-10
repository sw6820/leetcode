class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a=1
        if 0 in nums: return 0
        for i in nums:
            a*=(1 if i>0 else -1)
        return a