class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        for i,v in enumerate(nums):
            for j,k in enumerate(nums):
                if i!=j and v>k:l[i]+=1
        return l
                    
        