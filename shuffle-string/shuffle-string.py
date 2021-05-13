from collections import defaultdict
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r=['']*len(s)
        for i,c in enumerate(s):
            r[indices[i]]=c
        return ''.join(r)
        
###