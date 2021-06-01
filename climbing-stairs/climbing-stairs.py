class Solution:
    def climbStairs(self, n: int) -> int:
        d=[0]*(46)
        d[0],d[1]=1,1
        for i in range(2,46):
            d[i]=d[i-1]+d[i-2]
        return d[n]