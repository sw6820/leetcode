class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)<2: return [*map(str,nums)]
        rst=[]
        s=e=0
        while e<len(nums):
            if s==e: 
                e+=1
                continue
            if nums[e]-nums[e-1]==1:
                e+=1
            else:
                if e-s==1: 
                    rst.append(str(nums[s]))
                    s=e
                else:
                    rst.append(str(nums[s])+'->'+str(nums[e-1]))
                    s=e
                    e+=1
        if s==len(nums)-1:
            rst.append(str(nums[s]))
        else:
            rst.append(str(nums[s])+'->'+str(nums[e-1]))
        return rst
            