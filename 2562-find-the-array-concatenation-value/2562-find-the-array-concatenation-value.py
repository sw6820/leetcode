class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        r,s,e=0,0,len(nums)-1        
        while s<e:
            r+=int(str(nums[s])+str(nums[e]))
            s+=1
            e-=1
        return r+(nums[s]if s==e else 0)
            