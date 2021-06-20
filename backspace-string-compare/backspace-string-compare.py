class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a,b='',''
        for i in s:
            if i=='#':
                a=a[:len(a)-1] if a else ''
            else:
                a+=i
        for i in t:
            if i=='#':
                b=b[:len(b)-1] if a else ''
            else:
                b+=i
        return a==b