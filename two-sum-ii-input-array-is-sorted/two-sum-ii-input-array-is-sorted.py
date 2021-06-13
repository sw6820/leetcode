class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s,e=0,len(numbers)-1
        while s<e:
            t=numbers[s]+numbers[e]
            if t<target:s+=1
            elif t>target:e-=1
            else: return [s+1,e+1]