class Solution:
    def sortSentence(self, s: str) -> str:
        l=sorted(s.split(),key=lambda x: x[-1])
        r=''
        for i in l:
           r+=i[:-1]+' ' 
        return r.strip()