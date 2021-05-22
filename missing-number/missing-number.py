class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=[0]*(len(nums)+1)
        for i in nums:
            n[i]+=1
        print(n)
        for i,v in enumerate(n):
            if not v: return i