class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        a=[0,1]
        for i in range(2,n+1):
            a.append(a[i//2]+a[i//2+1] if i&1 else a[i//2])        
        return max(a[:n+1])