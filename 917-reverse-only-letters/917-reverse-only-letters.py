class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st=[]
        r=''
        for c in s:
            if c.isalpha():
                st.append(c)
        for c in s:            
            r+= st.pop() if c.isalpha() else c
        return r