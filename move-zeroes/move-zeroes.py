class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n,z=[],[]
        c,idx=0,0
        while c<len(nums):
            if not nums[idx]:nums.append(nums.pop(idx))
            else: idx+=1
            c+=1