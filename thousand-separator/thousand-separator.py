class Solution:
    def thousandSeparator(self, n: int) -> str:
        s,t='',str(n)[::-1]
        for i in range(0,len(str(n))//3+1):
            s+=t[3*i:3*i+3]+'.'                
        return s[::-1].strip('.')