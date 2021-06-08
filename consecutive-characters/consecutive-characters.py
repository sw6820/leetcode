class Solution:
    def maxPower(self, s: str) -> int:
        l=len(s)
        if l==1: return 1
        st,en,m=0,1,0
        while st<l and en<l:
            if s[st]==s[en]: en+=1
            else:
                m=max(m,en-st)
                st=en
        m=max(m,en-st)
        return m