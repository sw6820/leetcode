from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0
        def xor(l):
            if len(l)==1: return l[0]
            else:
                r=l[0]
                for i in l[1:]:
                    r^=i
                return r
        for i in range(1,len(nums)+1):
            for j in list(combinations(nums,i)):
                s+=xor(j)
        return s
        