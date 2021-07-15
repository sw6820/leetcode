class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s,t=sorted(s),sorted(t)
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else: return t[j]
        return t[-1]