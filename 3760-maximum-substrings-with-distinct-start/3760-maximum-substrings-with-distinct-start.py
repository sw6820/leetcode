class Solution:    
    def maxDistinct(self, s: str) -> int:
        from collections import defaultdict
        d=defaultdict(bool)
        for c in s:
            if not d[c]:
                d[c]=True
        return len(d)

        

        