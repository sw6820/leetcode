class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m,r=0,0
        for i in gain:
            r+=i
            m=max(m,r)
        return m