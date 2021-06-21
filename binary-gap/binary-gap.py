class Solution:
    def binaryGap(self, n: int) -> int:
        idx=[i for i,v in enumerate(bin(n)) if v=='1']        
        m=0
        for i in range(len(idx)-1):
            m=max(m,idx[i+1]-idx[i])
        return m