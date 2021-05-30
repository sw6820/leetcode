class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x:-x)
        s=sum(nums)
        for i in range(1,len(nums)//2+2):
            a=sum(nums[:i])
            if a>s-a:return nums[:i]
            
            