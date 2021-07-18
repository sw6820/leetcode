class Solution:
    def minOperations(self, s: str) -> int:
        l=len(s)
        c=sum(1 for i,v in enumerate(s) if (i&1)^int(v))        
        return min(c,l-c)