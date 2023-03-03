class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            if i*i==n*(n+1)//2: return i
        return -1
            
            
            