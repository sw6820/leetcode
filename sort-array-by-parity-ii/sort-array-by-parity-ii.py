class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        r=[0]*len(nums)
        o,e=1,0
        for i in nums:
            if i%2:
                r[o]=i
                o+=2
            else:
                r[e]=i
                e+=2
        return r
            