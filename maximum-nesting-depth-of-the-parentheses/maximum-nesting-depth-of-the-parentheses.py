class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        m=0
        for i in s:
            if i=='(':
                st.append('(')
                m=max(m,len(st))
            elif i==')':
                st.pop()
        return m