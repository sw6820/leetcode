class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        v=0
        l,r,lm,rm=0,len(height)-1,0,0
        while l<r:
            lm,rm=max(lm,height[l]),max(rm,height[r])
            if lm<rm:
                v+=lm-height[l]
                l+=1
            else:
                v+=rm-height[r]
                r-=1
        return v